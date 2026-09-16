/* Exact Sutherland viscosity with independently specified constant Prandtl. */

#ifndef sutherlandPrTransport_H
#define sutherlandPrTransport_H

#include "sutherlandTransport.H"

namespace Foam
{

template<class Thermo>
class sutherlandPrTransport : public sutherlandTransport<Thermo>
{
    scalar Pr_;

public:
    explicit sutherlandPrTransport(const dictionary& dict)
    :
        sutherlandTransport<Thermo>(dict),
        Pr_(dict.subDict("transport").get<scalar>("Pr"))
    {}

    sutherlandPrTransport(const Thermo& thermo, const dictionary& dict)
    :
        sutherlandTransport<Thermo>(thermo, dict),
        Pr_(dict.subDict("transport").get<scalar>("Pr"))
    {}

    sutherlandPrTransport(const word& name, const sutherlandPrTransport& rhs)
    :
        sutherlandTransport<Thermo>(name, rhs),
        Pr_(rhs.Pr_)
    {}

    inline autoPtr<sutherlandPrTransport> clone() const
    {
        return autoPtr<sutherlandPrTransport>::New(*this);
    }

    inline static autoPtr<sutherlandPrTransport> New(const dictionary& dict)
    {
        return autoPtr<sutherlandPrTransport>::New(dict);
    }

    static word typeName()
    {
        return "sutherlandPr<" + Thermo::typeName() + '>';
    }

    inline scalar kappa(const scalar p, const scalar T) const
    {
        return this->mu(p, T)*this->Cp(p, T)/Pr_;
    }

    inline scalar alphah(const scalar p, const scalar T) const
    {
        return this->mu(p, T)/Pr_;
    }
};

} // End namespace Foam

#endif
