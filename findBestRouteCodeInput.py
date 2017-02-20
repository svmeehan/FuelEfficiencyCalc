from fleet import *
from Itinerary import *
import sys

if len(sys.argv) != 7:
	print('Program needs 6 arguments, 5 space sperated airport codes and an aircraft code')
else:

	itinerary = Itinerary(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
	fleet = Fleet(itinerary)

	fleet.flyAllAircraft()
	#fleet.getBestRouteSimple()
	fleet.getBestRouteWithOptimumFuel()