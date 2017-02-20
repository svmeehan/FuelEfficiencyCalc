import csv

class AircraftAtlas:

    def __init__(self):
        self.loadData()    #load data in our constructor


    def loadData(self, aircraftCSV='aircraft.csv'):
        """ Create our dictionary containing all the aircraft """
        aircraftDict = {}
        
        with open(aircraftCSV, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                #if imperial convert to metric
                if line[2] == 'imperial':
                    range = float(line[4]) * 8 / 5
                else:
                    range = float(line[4])
                aircraftDict[line[0]] = [line[1], line[3], range]
            self.aircraftDict = aircraftDict

    def getAircraft(self, code):
        """ return aircraft details in a list for a code """
    	
        return self.aircraftDict[code.upper()]