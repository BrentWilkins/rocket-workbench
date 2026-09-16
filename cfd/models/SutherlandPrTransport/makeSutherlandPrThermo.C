#include "psiThermo.H"
#include "makeThermo.H"

#include "specie.H"
#include "perfectGas.H"
#include "hConstThermo.H"
#include "sensibleInternalEnergy.H"
#include "thermo.H"
#include "hePsiThermo.H"
#include "pureMixture.H"

#include "sutherlandPrTransport.H"

namespace Foam
{

makeThermos
(
    psiThermo,
    hePsiThermo,
    pureMixture,
    sutherlandPrTransport,
    sensibleInternalEnergy,
    hConstThermo,
    perfectGas,
    specie
);

}
