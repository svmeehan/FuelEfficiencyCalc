import os
import csv

class DistanceTable:
    '''This object stores the distances already calculated'''
    distanceDictionary={}

    def __init__(self, file = 'distancetable.csv'):
        if os.path.isfile(file):
            self.loadData()

    def loadData(self, csvFile = 'distancetable.csv'):
        dictionary = {}
        with open(csvFile, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                dictionary[line[0]] = line[1]
            self.distanceDictionary = dictionary

    def saveData(self, dictionary = self.distanceDictionary, toFile = 'distancetable.csv'):
        with open(toFile, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(dictionary.items())

    def addNewDistance(self, airport1, airport2, distance):
        distanceDictionary[airport1+'-'+airport2] = distance

    def getDistance(self, airport1, airport2):
        return distanceDictionary[airport1+'-'+airport2]
