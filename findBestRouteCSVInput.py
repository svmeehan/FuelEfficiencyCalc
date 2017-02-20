from fleet import *
from Itinerary import *
import sys
import csv

def main():
	if len(sys.argv) == 2:
		print('Running with user specified CSV file:', sys.argv[1])
		optimumPathList = readFileAndCalculateOptimum(sys.argv[1])
	else:
		print('Running with default file: testroutes.csv')
		optimumPathList = readFileAndCalculateOptimum()
		#print(optimumPathList)
		writeOptimum2File(optimumPathList)


def readFileAndCalculateOptimum(testRoutesCSV='testroutes.csv'):
	optimumPathList = []
	with open(testRoutesCSV, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		for line in reader:
			if len(line) == 6:	#only accept itineraries with 
				itinerary = Itinerary(line[0], line[1], line[2], line[3], line[4], line[5])
				fleet = Fleet(itinerary)
				fleet.flyAllAircraft()
				#fleet.getBestRouteSimple()
				optimumPathList.append(fleet.getBestRouteWithOptimumFuel())
			else:
				print('invalid route')
		return optimumPathList


def writeOptimum2File(optimumPaths, bestRoutesCSV='bestroutes.csv'):
	with open(bestRoutesCSV, 'w') as f:
		for path in optimumPaths:
			f.write(path+'\n')

main()
