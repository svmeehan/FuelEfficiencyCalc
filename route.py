import distanceCalculator	#a file containing the functions to calculate great circle distances

class Route:

	
	def __init__(self, airportList, AirportAtlas):
		""" Create a route from a list of airports. 
		Add in some extra variables to hold important info"""
		# we will create airport objects for the Route
		# all airports already exist in memory when we instantiate the AirportAtlas
		# However we do not want to reload the atlas every time we create a new route so we must pass it's name into the constructor
		self.home = AirportAtlas.getAirport(airportList[0])
		remainingAirports = []
		for airportCode in airportList:
			remainingAirports.append(AirportAtlas.getAirport(airportCode))
		self.airports2Visit = remainingAirports[1:]	#airports that are'nt the home airport
		self.currentAirport = self.home		#we start at the home airport
		self.nextAirportIndex = 0			#index of the next airport
		self.nextAirport = self.airports2Visit[0]
		self.savedDistances = []	#we will store calculated sitances here
		self.savedCosts = []		#we will store calculated costs here
		self.isPossible = True		#if a route is impossible we need to know


	def getDistance(self):
		if self.nextAirport != None:
			distance = distanceCalculator.calcDistanceWithObjects(self.currentAirport, self.nextAirport)
			#print('Calculating distance between '+self.currentAirport.airportName+' and '+self.nextAirport.airportName)
			#print('distance from', self.currentAirport.airportName, '->', self.nextAirport.airportName, ':', distance, 'km')
			#print('Total Cost: ', distance * self.currentAirport.currency.rate)
			self.savedDistances.append(distance) #If you keep using the get distance method you will add too many values to list
			self.savedCosts.append(distance * self.currentAirport.currency.rate) # Move This
		else:
			print('Already at end of route.')

	def go2NextAirport(self):
		if self.nextAirportIndex < len(self.airports2Visit):
			self.getDistance()
			#print('I\'m at', self.currentAirport.airportName, 'going to', self.nextAirport.airportName)
			self.currentAirport = self.nextAirport 	#move to next airport
			self.nextAirportIndex += 1
			try:
				self.nextAirport = self.airports2Visit[self.nextAirportIndex]	
			except IndexError:	#if the next airport is not in the list it means we have to go home next
				self.nextAirport = self.home
		elif self.nextAirportIndex == len(self.airports2Visit):
			#print('I\'m at', self.currentAirport.airportName, 'going to', self.nextAirport.airportName)
			self.getDistance()
			self.nextAirportIndex += 1
		else:
			self.currentAirport = self.home
			self.nextAirport = None 	#other methods check this as a way to tell when a route is done
			#print('Reached end of route')
			#print(self.toString())
			#print('Total Distance:', sum(self.savedDistances),'km for', len(self.savedDistances), 'stages')

	def completeRoute(self):
		""" Go to end of route through all airports, recording distance"""
		for i in range((len(self.airports2Visit) + 1) - self.nextAirportIndex):
			self.go2NextAirport()

	def getTotalDistance(self):
		""" sum the saved distance if the route is complete"""
		#need to stop people from using this before route is complete
		if self.currentAirport == self.home and self.nextAirport == None:
			return sum(self.savedDistances)
		else:
			print('Route not complete.')


	def getTotalCost(self):
		#need to stop people from using this before route is complete
		if self.currentAirport == self.home and self.nextAirport == None:
			return sum(self.savedCosts)
		else:
			print('Route not complete.')


	def toString(self):
		routeString = (self.home.code)
		for airport in self.airports2Visit:
			routeString += (',' + airport.code)
		routeString += (',' + self.home.code)
		return routeString	