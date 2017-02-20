from fleet import *
from Itinerary import *

it = Itinerary('DUB', 'LHR', 'SFO', 'JFK', 'EIN', '747')
fleet = Fleet(it)

fleet.flyAllAircraft()
#fleet.getBestRouteSimple()
fleet.getBestRouteWithOptimumFuel()