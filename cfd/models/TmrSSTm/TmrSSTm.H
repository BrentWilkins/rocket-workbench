/*---------------------------------------------------------------------------*\
  TMR standard Menter SSTm compatibility model for OpenFOAM v2512.

  This file is distributed under the GNU General Public License v3 or later,
  consistently with OpenFOAM.  It derives from the packaged v2512 kOmegaSST
  implementation and changes only the equations documented by NASA TMR for
  the original standard SST/SSTm definition.
\*---------------------------------------------------------------------------*/

#ifndef TmrSSTm_H
#define TmrSSTm_H

#include "kOmegaSST.H"

namespace Foam
{
namespace RASModels
{

template<class BasicTurbulenceModel>
class TmrSSTm
:
    public kOmegaSST<BasicTurbulenceModel>
{
    TmrSSTm(const TmrSSTm&) = delete;
    void operator=(const TmrSSTm&) = delete;

protected:
    virtual tmp<volScalarField> F1(const volScalarField& CDkOmega) const;
    virtual tmp<volScalarField> F2() const;
    virtual tmp<volScalarField> F23() const;
    virtual void correctNut(const volScalarField& S2);
    virtual void correctNut();

public:
    typedef typename BasicTurbulenceModel::alphaField alphaField;
    typedef typename BasicTurbulenceModel::rhoField rhoField;
    typedef typename BasicTurbulenceModel::transportModel transportModel;

    TypeName("TmrSSTm");

    TmrSSTm
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

    virtual ~TmrSSTm() = default;

    //- Solve the original incompressible SSTm transport equations without
    //  the generic v2512 isotropic-divergence source corrections.
    virtual void correct();
};

} // End namespace RASModels
} // End namespace Foam

#ifdef NoRepository
    #include "TmrSSTm.C"
#endif

#endif
