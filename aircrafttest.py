import unittest
from Aircraft import *
from route import *
from airport import *

class TestAircraft(unittest.TestCase):

	airportAtlas = AirportAtlas()

	def test_aircraft_constructor(self):
		simpleRoute = Route(['DUB', 'LHR', 'EIN'], self.airportAtlas)
		testAircraft = Aircraft('747', 1000, simpleRoute)
		self.assertEqual(testAircraft.code, '747')
		self.assertEqual(testAircraft.flightRadius, 1000)

	def test_aircraft_flyNextStage_valid(self):
		simpleRoute = Route(['DUB', 'LHR', 'EIN'], self.airportAtlas)
		testAircraft = Aircraft('747', 1000, simpleRoute)
		self.assertEqual(testAircraft.route.currentAirport.code, 'DUB')
		testAircraft.flyNextStage()
		self.assertEqual(testAircraft.route.currentAirport.code, 'LHR')

	def test_aircraft_flyNextStage_out_of_range(self):
		simpleRoute = Route(['DUB', 'LHR', 'EIN'], self.airportAtlas)
		testAircraft = Aircraft('747', 50, simpleRoute)
		self.assertEqual(testAircraft.route.currentAirport.code, 'DUB')
		testAircraft.flyNextStage()
		self.assertEqual(testAircraft.route.isPossible, False)

	def test_aircraft_completeRoute_valid(self):
		simpleRoute = Route(['DUB', 'LHR', 'EIN'], self.airportAtlas)
		testAircraft = Aircraft('747', 1000, simpleRoute)
		self.assertEqual(testAircraft.route.currentAirport.code, 'DUB')
		testAircraft.completeRoute()
		self.assertEqual(testAircraft.route.currentAirport.code, 'DUB')

	def test_aircraft_calculateOptimumFuel_route_not_complete(self):
		simpleRoute = Route(['DUB', 'LHR', 'EIN'], self.airportAtlas)
		testAircraft = Aircraft('747', 1000, simpleRoute)
		testAircraft.calculateOptimumFuel()
		self.assertEqual(testAircraft.fuelBought, [])

	def test_aircraft_calculateOptimumFuel_valid(self):
		simpleRoute = Route(['DUB', 'LHR', 'EIN'], self.airportAtlas)
		testAircraft = Aircraft('747', 1000, simpleRoute)
		testAircraft.completeRoute()
		testAircraft.calculateOptimumFuel()
		self.assertEqual(len(testAircraft.fuelBought), 4)


	def test_aircraft_buyFuel(self):
		simpleRoute = Route(['DUB', 'LHR', 'EIN'], self.airportAtlas)
		testAircraft = Aircraft('747', 1000, simpleRoute)
		fuelBought = testAircraft.buyFuel(testAircraft.route.currentAirport, 1000)
		self.assertEqual(fuelBought, 1000)
		fuelBought = testAircraft.buyFuel(testAircraft.route.currentAirport, 1500)
		self.assertEqual(fuelBought, 1000)
		fuelBought = testAircraft.buyFuel(testAircraft.route.currentAirport, 800)
		self.assertEqual(fuelBought, 800)



if __name__ == '__main__':
    unittest.main()