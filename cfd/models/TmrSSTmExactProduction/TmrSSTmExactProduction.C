/*---------------------------------------------------------------------------*\
  NASA TMR SSTm P = mu_t S^2 production definition for OpenFOAM v2512.
\*---------------------------------------------------------------------------*/

#include "TmrSSTmExactProduction.H"

namespace Foam
{
namespace RASModels
{

template<class BasicTurbulenceModel>
tmp<volScalarField::Internal>
TmrSSTmExactProduction<BasicTurbulenceModel>::GbyNu0
(
    const volTensorField& /* gradU */,
    const volScalarField& S2
) const
{
    return tmp<volScalarField::Internal>::New
    (
        IOobject::scopedName(this->type(), "GbyNu"),
        S2()
    );
}


template<class BasicTurbulenceModel>
TmrSSTmExactProduction<BasicTurbulenceModel>::TmrSSTmExactProduction
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
    TmrSSTmKOnlyLimiter<BasicTurbulenceModel>
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

} // End namespace RASModels
} // End namespace Foam
