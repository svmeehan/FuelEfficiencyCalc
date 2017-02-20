import csv
import airport
import distanceCalculator

class Aircraft:
    """
    Aircraft class: An airplane has to be fuelled before it can take off
    """
    __fuel = 0 # private attribute containing current fuel in aircraft

    def __init__(self, code, flightRadius, route):
        """ We create a constructor that takes an aircraft code distance and a route object.
        We also define a placeholder to record the fuel we buy.
        It will be a 2D list """
        self.code = code
        self.flightRadius = flightRadius
        self.route = route
        self.fuelBought = []

    def flyNextStage(self):
        """ Moves the aircraft from one airport to another using the route method.
        It implements checks to make sure the trip is possible """
        if  self.route.isPossible and self.route.nextAirport != None:
            self.route.go2NextAirport()
            #print('Current Airport:', self.route.currentAirport.airportName)
        if self.route.savedDistances[-1] > self.flightRadius:
            self.route.isPossible = False
            # if you can't make it flag the root as not possible

    def completeRoute(self):
        """ We fly all the stages using this function.
        Once the route is no longer possible we abandon it """
        while self.route.isPossible == True and self.route.nextAirport != None:
            self.flyNextStage()

    def calculateOptimumFuel(self):
        """ Algorithm to determine the most fuel efficient route.
        The general rules are:
        Only for possible routes, if there is a cheaper aiport in the reamining route buy enough fuel to get there
        else if you are at a minimum for the rest of the route fill up fully
        else buy the minimum to get you where you are going """
        if self.route.currentAirport == self.route.home and self.route.nextAirport == None and self.route.isPossible:
            #print('inCalculateOptimumFuel')
            currencyRates = self.getCurrencyRatesList()
            routeTotalDistance = sum(self.route.savedDistances)
            maxFuel = self.flightRadius
            currentFuel = 0
            totalFuelBought = 0
            allAirports = [self.route.home] + self.route.airports2Visit + [self.route.home]
            #print(len(currencyRates), len(self.route.savedDistances), len(allAirports))
            #currencyRates += [currencyRates[0]]
            for index in range(len(currencyRates)):
                #print(totalFuelBought, routeTotalDistance)
                rates2Consider = currencyRates[index:]
                currentRate = rates2Consider[0]
                futureRates = rates2Consider[1:]
                futureRates.append(currencyRates[0])
                #print(futureRates)
                #print(allAirports[index].airportName, currentRate)
                if currentRate <= min(futureRates):         #buy fuel if at local min
                    #print('Min fuel Price: Filling tank')
                    fuelBought = self.buyFuel(allAirports[index], self.flightRadius - currentFuel)
                    currentFuel += fuelBought
                    totalFuelBought += fuelBought
                elif currentFuel < self.route.savedDistances[index]:    #buy fuel  if you need it to get to the next airport
                # Check if fuel is needed for next stage
                    requiredFuel = self.route.savedDistances[index] - currentFuel
                    fuelBought = self.buyFuel(allAirports[index], requiredFuel)
                    currentFuel += fuelBought
                    totalFuelBought += fuelBought
                else:
                    #print('No fuel desired at:', allAirports[index].airportName)
                    self.buyFuel(allAirports[index], 0)
                
                currentFuel -= self.route.savedDistances[index]     #remove fuel based on the distance to travel
            
            fuelNeeded2FillTank = self.flightRadius - currentFuel
            #print(fuelNeeded2FillTank)
            fillTank = self.buyFuel(self.route.home, fuelNeeded2FillTank) #we fill up our tank at the end so everything is fair
            fuelBought += fillTank
            currentFuel += fillTank
            #print(currentFuel,'==', self.flightRadius)


                #while totalFuelBought < (routeTotalDistance + self.flightRadius):          
        else:
            print('Route not complete.')

    def buyFuel(self, airport, amount):
        """ Buy Fuel of the amount decided. If you can't fit it just buy the maximum """
        maxFuelBuyable = self.flightRadius
        if amount <= maxFuelBuyable:
            self.fuelBought.append([airport.currency.rate, amount])
            #print('adding', amount, 'fuel at', airport.airportName)
            return amount
        else:
            self.fuelBought.append([airport.currency.rate, maxFuelBuyable])
            #print('adding', maxFuelBuyable, 'fuel at', airport.airportName)
            return maxFuelBuyable


    def getCurrencyRatesList(self):
        """ Return the currency rates for all airports in the route in order"""
        currencyRates = [self.route.home.currency.rate]
        for airport in self.route.airports2Visit:
            currencyRates.append(airport.currency.rate)
        return currencyRates


    def printOptimumStrategy(self):
        """ Method to print the fuel strategy to the terminal """
        index = 0
        #print(self.fuelBought)
        for purchase in self.fuelBought:
            if index ==0:
                print('\nBought', purchase[1], 'litres of fuel at a price of', purchase[0], 'per litre at', self.route.home.airportName)
            else:
                try:
                    print('Bought', purchase[1], 'litres of fuel at a price of', purchase[0], 'per litre at', self.route.airports2Visit[index-1].airportName)
                except IndexError:
                    print('Bought', purchase[1], 'litres of fuel at a price of', purchase[0], 'per litre at', self.route.home.airportName)
            index += 1





class AircraftAtlas:

    def __init__(self):
        self.loadData()


    def loadData(self, aircraftCSV='aircraft.csv'):
        aircraftDict = {}
        
        with open(aircraftCSV, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                #if imperial convert to metric
                if line[2] == 'imperial':
                    flightRadius = float(line[4]) * 8 / 5
                else:
                    flightRadius = float(line[4])
                aircraftDict[line[0]] = [line[1], line[3], flightRadius]
            self.aircraftDict = aircraftDict

    def getAircraft(self, code):
        return self.aircraftDict[code]