import math as ma

def calcPhi(latitude):
    phi = 90 - (latitude)
    return ma.radians(phi)


def calcDistance(lat1, lon1, lat2, lon2):
    rE = 6371
    phi1 = calcPhi(lat1)
    phi2 = calcPhi(lat2)
    theta1 = ma.radians(lon1)
    theta2 = ma.radians(lon2)
    distance = ma.acos((ma.sin(phi1) * ma.sin(phi2) * ma.cos(theta1 - theta2)) + (ma.cos(phi1) * ma.cos(phi2))) * rE
    return int(distance)

def calcDistanceWithObjects(airport1, airport2):
    lat1 = airport1.lat
    lat2 = airport2.lat
    lon1 = airport1.long
    lon2 = airport2.long
    distance = calcDistance(lat1, lon1, lat2, lon2)
    return distance