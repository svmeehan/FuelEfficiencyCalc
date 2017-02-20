import csv

class Currency:
    '''country, currency name, currency rate (ratio to euro)'''
    def __init__(self, currencyCode, currencyName, currencyRate):
        self.currencyCode = currencyCode
        self.currencyName = currencyName
        self.rate = currencyRate

class CurrencyAtlas:
    ''' We create a dictionary where the key is country. This key is chosen over currency code as it is available to airport objects'''
    currencyDict = {}
    country2CurrencyCodeDict = {}

    #CONSTRUCTOR
    def __init__(self):
        self.loadData()


    def loadData(self, countryCurrencyCSV='countrycurrency.csv', currencyRatesCSV='currencyrates.csv'):
        country2CurrencyCodeDict = {}
        currencyDict = {}
        
        with open(countryCurrencyCSV, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                country2CurrencyCodeDict[line[0]] = line[14]
                #key is country name. Value is currency code
            self.country2CurrencyCodeDict = country2CurrencyCodeDict

        with open(currencyRatesCSV, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                currencyDict[line[1]] = Currency(line[1], line[0], float(line[2]))
                #key is currency code, value is a currency object
            self.currencyDict = currencyDict

    def getCurrency(self, country):
        return self.currencyDict[self.country2CurrencyCodeDict[country]]
        