/*---------------------------------------------------------------------------*\
  NASA TMR SSTm P = mu_t S^2 production definition for OpenFOAM v2512.
\*---------------------------------------------------------------------------*/

#ifndef TmrSSTmExactProduction_H
#define TmrSSTmExactProduction_H

#include "TmrSSTmKOnlyLimiter.H"

namespace Foam
{
namespace RASModels
{

template<class BasicTurbulenceModel>
class TmrSSTmExactProduction
:
    public TmrSSTmKOnlyLimiter<BasicTurbulenceModel>
{
    TmrSSTmExactProduction(const TmrSSTmExactProduction&) = delete;
    void operator=(const TmrSSTmExactProduction&) = delete;

protected:
    //- Return P/nut = S^2 as specified for the NASA TMR SSTm variant.
    virtual tmp<volScalarField::Internal> GbyNu0
    (
        const volTensorField& gradU,
        const volScalarField& S2
    ) const;

public:
    typedef typename BasicTurbulenceModel::alphaField alphaField;
    typedef typename BasicTurbulenceModel::rhoField rhoField;
    typedef typename BasicTurbulenceModel::transportModel transportModel;

    TypeName("TmrSSTmExactProduction");

    TmrSSTmExactProduction
    (
        const alphaField& alpha,
        const rhoField& rho,
        const volVectorField& U,
        const surfaceScalarField& alphaRhoPhi,
        const surfaceScalarField& phi,
        const transportModel& transport,
        const word& propertiesName = turbulenceModel::propertiesName,
        const word& type = typeName
    );

    virtual ~TmrSSTmExactProduction() = default;
};

} // End namespace RASModels
} // End namespace Foam

#ifdef NoRepository
#include "TmrSSTmExactProduction.C"
#endif

#endif
