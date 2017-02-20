import Itinerary

#home = input('Enter home airport code: ')
#airport1 = input('Enter another airport: ')
#airport2 = input('Enter another airport: ')
#airport3 = input('Enter another airport: ')
#airport4 = input('Enter another airport: ')

#it = Itinerary.Itinerary(home, airport1, airport2, airport3, airport4)
it = Itinerary.Itinerary('DUB', 'LHR', 'SFO', 'JFK', 'EIN', '747')
it.getAllRoutes()
#it.getOptionalRoutes()

fleet = it.createAircraft('747')

#print(al[0].route.currentAirport.airportName)
#print(al[2].route.currentAirport.airportName)

routeTotals = []
routeCost = []
optimumFuelPrices = []
optimalPurchases = []


#for airplane in fleet:
#	airplane.route.completeRoute()
#	routeTotals.append(airplane.route.getTotalDistance())
#	routeCost.append(airplane.route.getTotalCost())
#	print('Total Cost:', airplane.route.getTotalCost())

for airplane in fleet:
	airplane.completeRoute()
	if airplane.route.isPossible == True:
		routeTotals.append(airplane.route.getTotalDistance())
		routeCost.append(airplane.route.getTotalCost())
		print('Total Cost:', round(airplane.route.getTotalCost(), 2), 'euros')

print(len(routeTotals), 'planes succeeded.', len(fleet) - len(routeTotals), 'failed.')


#print(routeTotals)
#print(routeCost)
if len(routeCost) > 0:
	bestRoute = min(routeCost)
	routeStopsIndex = routeCost.index(bestRoute)
	bestRouteStops = fleet[routeStopsIndex].route.toString()
	print('Best Route:', bestRouteStops, round(bestRoute, 2), 'euros')
else:
	print('No route possible')

print(fleet[0].route.toString())
fleet[76].calculateOptimumFuel()
print(fleet[0].fuelBought)
solved = 0
for airplane in fleet:
	if airplane.route.isPossible == True:
		solved += 1
		airplane.calculateOptimumFuel()
		optimalPurchases.append(airplane.fuelBought)
		print(airplane.fuelBought)
		totalPrice = 0
		print(airplane.route.toString())
		for purchase in airplane.fuelBought:
			print(purchase[0], purchase[1])
			totalPrice += purchase[0] * purchase[1]
		optimumFuelPrices.append(round(totalPrice,2))
print('Best Price Available', min(optimumFuelPrices))
bestFuelPriceIndex = optimumFuelPrices.index(min(optimumFuelPrices))
bestFuelRouteStops = fleet[bestFuelPriceIndex].route.toString()
print('solved', solved, 'airplane')
print(bestFuelRouteStops)
print(optimalPurchases[bestFuelPriceIndex])
#print(fleet[76].fuelBought)