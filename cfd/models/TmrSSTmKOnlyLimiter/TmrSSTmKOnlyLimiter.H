/*---------------------------------------------------------------------------*\
  NASA TMR SSTm production-limiter parity correction for OpenFOAM v2512.
\*---------------------------------------------------------------------------*/

#ifndef TmrSSTmKOnlyLimiter_H
#define TmrSSTmKOnlyLimiter_H

#include "TmrSSTm.H"

namespace Foam
{
namespace RASModels
{

template<class BasicTurbulenceModel>
class TmrSSTmKOnlyLimiter
:
    public TmrSSTm<BasicTurbulenceModel>
{
    TmrSSTmKOnlyLimiter(const TmrSSTmKOnlyLimiter&) = delete;
    void operator=(const TmrSSTmKOnlyLimiter&) = delete;

public:
    typedef typename BasicTurbulenceModel::alphaField alphaField;
    typedef typename BasicTurbulenceModel::rhoField rhoField;
    typedef typename BasicTurbulenceModel::transportModel transportModel;

    TypeName("TmrSSTmKOnlyLimiter");

    TmrSSTmKOnlyLimiter
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

    virtual ~TmrSSTmKOnlyLimiter() = default;

    //- Use unlimited production in omega and the factor-20 limiter only in k.
    virtual void correct();
};

} // End namespace RASModels
} // End namespace Foam

#ifdef NoRepository
#include "TmrSSTmKOnlyLimiter.C"
#endif

#endif
