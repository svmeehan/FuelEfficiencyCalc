import route
import airport

aa = airport.AirportAtlas()
airportList = ['DUB', 'LHR', 'SFO', 'JFK', 'EIN']
route = route.Route(airportList, aa)

print(route.home.currency.rate)
for airport in route.airports2Visit:
	print(airport.currency.rate)

#route.getDistance()
#route.go2NextAirport()
route.completeRoute()

#print(route.savedDistances)