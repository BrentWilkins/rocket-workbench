/*---------------------------------------------------------------------------*\
  NASA TMR standard SSTm equation deltas for OpenFOAM v2512.
\*---------------------------------------------------------------------------*/

#include "TmrSSTm.H"
#include "bound.H"
#include "fvOptions.H"

namespace Foam
{
namespace RASModels
{

template<class BasicTurbulenceModel>
tmp<volScalarField> TmrSSTm<BasicTurbulenceModel>::F1
(
    const volScalarField& CDkOmega
) const
{
    const tmp<volScalarField> CDkOmegaPlus = max
    (
        CDkOmega,
        dimensionedScalar(dimless/sqr(dimTime), 1.0e-20)
    );

    const tmp<volScalarField> arg1 = min
    (
        max
        (
            (scalar(1)/this->betaStar_)*sqrt(this->k_)
           /(this->omega_*this->y_),
            scalar(500)*(this->mu()/this->rho_)
           /(sqr(this->y_)*this->omega_)
        ),
        (4*this->alphaOmega2_)*this->k_
       /(CDkOmegaPlus*sqr(this->y_))
    );

    return tanh(pow4(arg1));
}


template<class BasicTurbulenceModel>
tmp<volScalarField> TmrSSTm<BasicTurbulenceModel>::F2() const
{
    const tmp<volScalarField> arg2 = max
    (
        (scalar(2)/this->betaStar_)*sqrt(this->k_)
       /(this->omega_*this->y_),
        scalar(500)*(this->mu()/this->rho_)
       /(sqr(this->y_)*this->omega_)
    );

    return tanh(sqr(arg2));
}


template<class BasicTurbulenceModel>
tmp<volScalarField> TmrSSTm<BasicTurbulenceModel>::F23() const
{
    // Standard SSTm has F2 only; OpenFOAM's optional rough-wall F3 is absent.
    return F2();
}


template<class BasicTurbulenceModel>
void TmrSSTm<BasicTurbulenceModel>::correctNut
(
    const volScalarField& /* S2 */
)
{
    const volScalarField Omega
    (
        sqrt(scalar(2))*mag(skew(fvc::grad(this->U_)))
    );

    this->nut_ = this->a1_*this->k_
       /max(this->a1_*this->omega_, this->b1_*F2()*Omega);
    this->nut_.correctBoundaryConditions();
    fv::options::New(this->mesh_).correct(this->nut_);

    BasicTurbulenceModel::correctNut();
}


template<class BasicTurbulenceModel>
void TmrSSTm<BasicTurbulenceModel>::correctNut()
{
    const volScalarField S2
    (
        2*magSqr(symm(fvc::grad(this->U_)))
    );
    correctNut(S2);
}


template<class BasicTurbulenceModel>
TmrSSTm<BasicTurbulenceModel>::TmrSSTm
(
    const alphaField& alpha,
    const rhoField& rho,
    const volVectorField& U,
    const surfaceScalarField& alphaRhoPhi,
    const surfaceScalarField& phi,
    const transportModel& transport,
    const word& propertiesName,
    const word& type
)
:
    kOmegaSST<BasicTurbulenceModel>
    (
        alpha,
        rho,
        U,
        alphaRhoPhi,
        phi,
        transport,
        propertiesName,
        type
    )
{
    if (type == typeName)
    {
        this->printCoeffs(type);
    }
}


template<class BasicTurbulenceModel>
void TmrSSTm<BasicTurbulenceModel>::correct()
{
    if (!this->turbulence_)
    {
        return;
    }

    const alphaField& alpha = this->alpha_;
    const rhoField& rho = this->rho_;
    const surfaceScalarField& alphaRhoPhi = this->alphaRhoPhi_;
    const volVectorField& U = this->U_;
    volScalarField& nut = this->nut_;
    fv::options& fvOptions(fv::options::New(this->mesh_));

    eddyViscosity<RASModel<BasicTurbulenceModel>>::correct();

    tmp<volTensorField> tgradU = fvc::grad(U);
    const volScalarField S2(this->S2(tgradU()));
    volScalarField::Internal GbyNu0(this->GbyNu0(tgradU(), S2));
    volScalarField::Internal G(this->GName(), nut*GbyNu0);

    this->omega_.boundaryFieldRef().updateCoeffs();
    this->omega_.boundaryFieldRef().template evaluateCoupled<coupledFvPatch>();

    const volScalarField CDkOmega
    (
        (2*this->alphaOmega2_)
       *(fvc::grad(this->k_) & fvc::grad(this->omega_))/this->omega_
    );

    const volScalarField F1(this->F1(CDkOmega));
    const volScalarField F23(this->F23());

    {
        const volScalarField::Internal gamma(this->gamma(F1));
        const volScalarField::Internal beta(this->beta(F1));

        GbyNu0 = this->GbyNu(GbyNu0, F23(), S2());

        tmp<fvScalarMatrix> omegaEqn
        (
            fvm::ddt(alpha, rho, this->omega_)
          + fvm::div(alphaRhoPhi, this->omega_)
          - fvm::laplacian(
                alpha*rho*this->DomegaEff(F1), this->omega_)
         ==
            alpha()*rho()*gamma*GbyNu0
          - fvm::Sp(
                alpha()*rho()*beta*this->omega_(), this->omega_)
          - fvm::SuSp
            (
                alpha()*rho()*(F1() - scalar(1))*CDkOmega()/this->omega_(),
                this->omega_
            )
          + alpha()*rho()*beta*sqr(this->omegaInf_)
          + this->Qsas(S2(), gamma, beta)
          + this->omegaSource()
          + fvOptions(alpha, rho, this->omega_)
        );

        omegaEqn.ref().relax();
        fvOptions.constrain(omegaEqn.ref());
        omegaEqn.ref().boundaryManipulate(this->omega_.boundaryFieldRef());
        solve(omegaEqn);
        fvOptions.correct(this->omega_);
        bound(this->omega_, this->omegaMin_);
    }

    {
        tmp<fvScalarMatrix> kEqn
        (
            fvm::ddt(alpha, rho, this->k_)
          + fvm::div(alphaRhoPhi, this->k_)
          - fvm::laplacian(alpha*rho*this->DkEff(F1), this->k_)
         ==
            alpha()*rho()*this->Pk(G)
          - fvm::Sp(
                alpha()*rho()*this->epsilonByk(F1, tgradU()), this->k_)
          + alpha()*rho()*this->betaStar_*this->omegaInf_*this->kInf_
          + this->kSource()
          + fvOptions(alpha, rho, this->k_)
        );

        tgradU.clear();

        kEqn.ref().relax();
        fvOptions.constrain(kEqn.ref());
        solve(kEqn);
        fvOptions.correct(this->k_);
        bound(this->k_, this->kMin_);
    }

    correctNut(S2);
}

} // End namespace RASModels
} // End namespace Foam
