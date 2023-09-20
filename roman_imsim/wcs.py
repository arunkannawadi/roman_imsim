import galsim
import galsim.roman as roman
from galsim.config import WCSBuilder,RegisterWCSType
from galsim.angle import Angle
from galsim.celestial import CelestialCoord

class RomanWCS(WCSBuilder):

    def buildWCS(self, config, base, logger):

        req = { 'SCA' : int,
                'ra'  : Angle,
                'dec' : Angle,
                'pa'  : Angle,
                'mjd' : float
              }

        kwargs, safe = galsim.config.GetAllParams(config, base, req=req)
        pointing = CelestialCoord(ra=kwargs['ra'], dec=kwargs['dec'])
        wcs = roman.getWCS(world_pos        = pointing,
                                PA          = kwargs['pa'],
                                date        = Time(kwargs['mjd'],format='mjd').datetime,
                                SCAs        = kwargs['SCA'],
                                PA_is_FPA   = True
                                )[kwargs['SCA']]
        return wcs

RegisterWCSType('RomanWCS', RomanWCS())