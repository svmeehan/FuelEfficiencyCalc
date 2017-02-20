import Aircraft

class Fleet:
	''' Code to instantiate and use multiple aircraft objects'''

	def __init__(self, itinerary):
		self.itinerary = itinerary
		self.aircraftList = self.createAircraft(itinerary.aircraftType)
		self.routeTotals = []
		self.routeCost = []
		self.optimumPurchases = []
		self.optimumFuelPrices = []


	def createAircraft(self, code):
		""" Create a unique aircraft for every route"""
		aircraftList = []
		print('\ncreating', len(self.itinerary.allRoutes), 'Aircraft')
		print('For Route:', self.itinerary.toString(), 'with aircraft', self.itinerary.aircraftType)
		aircraftAtlas = Aircraft.AircraftAtlas()
		flightRadius = aircraftAtlas.getAircraft(code)[2]
		for route in self.itinerary.allRoutes:
			aircraftList.append(Aircraft.Aircraft(code, flightRadius, route))
		return aircraftList


	def flyAllAircraft(self):
		""" Fly all the aircraft to the end of their routes """
		for airplane in self.aircraftList:
			airplane.completeRoute()
			if airplane.route.isPossible == True:
				self.routeTotals.append(airplane.route.getTotalDistance())
				self.routeCost.append(airplane.route.getTotalCost())
				#print('Total Cost:', round(airplane.route.getTotalCost(), 2), 'euros')

		print(len(self.routeTotals), 'planes succeeded.', len(self.aircraftList) - len(self.routeTotals), 'failed.')

	def getBestRouteSimple(self):
		""" Just buy fuel at the current airport for the next leg of the trip and pick the best one"""
		if len(self.routeCost) > 0:
			bestRoute = min(self.routeCost)
			routeStopsIndex = self.routeCost.index(bestRoute)
			bestRouteStops = self.aircraftList[routeStopsIndex].route.toString()
			print('Best Route:', bestRouteStops, round(bestRoute, 2), 'euros')
		else:
			print('No route possible')

	def getBestRouteWithOptimumFuel(self):
		""" Calculate the fuel required for all planes. The find out which was the cheapest  """
		if len(self.routeCost) > 0:
			for airplane in self.aircraftList:
				if airplane.route.isPossible == True:
					airplane.calculateOptimumFuel()
					self.optimumPurchases.append(airplane.fuelBought)
					#print(airplane.fuelBought)
					totalPrice = 0
					#print(airplane.route.toString())
					#print(airplane.fuelBought)
					for purchase in airplane.fuelBought:
						#print(purchase[0], purchase[1])
						totalPrice += purchase[0] * purchase[1]
					self.optimumFuelPrices.append(round(totalPrice,2))
				else:
					self.optimumFuelPrices.append(99999999999)	##pretty sure that's bigger than the earth...
					#to keep indexes right for airport retrival. None cannot be in a list for the min() function to work
			#print(self.optimumPurchases)
			bestFuelPriceIndex = self.optimumFuelPrices.index(min(self.optimumFuelPrices))
			#print(self.optimumFuelPrices.index(min(self.optimumFuelPrices)))
			bestFuelRouteStops = self.aircraftList[bestFuelPriceIndex].route.toString()
			print('\nBest Price Available', min(self.optimumFuelPrices), 'euros for route', bestFuelRouteStops)
			self.aircraftList[bestFuelPriceIndex].printOptimumStrategy()
			return(self.aircraftList[bestFuelPriceIndex].route.toString()+','+str(min(self.optimumFuelPrices)))

			#print(bestFuelRouteStops)
			#print(self.optimumPurchases[bestFuelPriceIndex])
		else:
			print('No Route Possible')
			return 'No valid Route'