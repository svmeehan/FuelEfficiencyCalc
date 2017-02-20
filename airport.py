import csv
import Currency

class Airport:
	#CONSTRUCTOR
	def __init__(self, airportID, airportName, cityName, country, code, icaoCode, lat, long, alt, timeOffset, DST, timeZone, CurrencyAtlas):
		self.airportID = airportID
		self.airportName = airportName
		self.cityName = cityName
		self.country = country
		self.code = code
		self.icaoCode = icaoCode
		self.lat = float(lat)
		self.long = float(long)
		self.alt = alt
		self.timeOffset = timeOffset
		self.DST = DST
		self.timeZone = timeZone
		try:
			self.currency = CurrencyAtlas.getCurrency(country)
		except KeyError:
			print('Error finding currency information for airport \''+self.airportName+'\' in country \''+country+'\':')
			print('    Data not available in dictionary')
			self.currency = None




class AirportAtlas:
	#airportList = []
	airportDict = {}
	#CONSTRUCTOR
	def __init__(self, airportFile='airport.csv'):
		self.loadData(airportFile)


	def loadData(self, csvFile):
		# We will open our currency atlas to add currency info to our airport objects
		CurrencyAtlas = Currency.CurrencyAtlas()

		dictionary = {}
		with open(csvFile, 'r') as f:
			reader = csv.reader(f, delimiter=',')
			for line in reader:
				dictionary[line[4]] = Airport(line[0], line[1], line[2], line[3], 
				                          line[4], line[5], line[6], line[7], 
				                          line[8], line[9], line[10], line[11], CurrencyAtlas)
			self.airportDict = dictionary


	def getAirport(self, code):
		try:
			return self.airportDict[code.upper()]
		except KeyError:
			print('Airport', code.upper(), 'does not exist')