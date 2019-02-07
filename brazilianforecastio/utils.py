import requests
from json import load
from geopy.distance import distance

airportStationJsonFile = "./staticdata/airport_weather_stations.json"

def compareDistancesBetweenStations(lat, lon, stationLat, stationLon, stationDistanceToCompare=None):
    stationDistance = distance((lat,lon),(stationLat,stationLon)).kilometers
    if stationDistanceToCompare is None or stationDistance < stationDistanceToCompare:
        return stationDistance
    else:
        return stationDistanceToCompare
    
def loadStationAirportJSON(p_airportStationJsonFile = None):
    if p_airportStationJsonFile is None:
        p_airportStationJsonFile = airportStationJsonFile
    with open(p_airportStationJsonFile) as airportStationFilePath:
        return load(airportStationFilePath)

def closestStation(myLat, myLon, p_airportStationJsonFile=None):
    airportSationData = loadStationAirportJSON(p_airportStationJsonFile)
    theClosestOne = airportSationData[0],compareDistancesBetweenStations(myLat,myLon, airportSationData[0]['Latitude'], airportSationData[0]['Longitude'])
    for station in airportSationData:
        newDistance = compareDistancesBetweenStations(myLat,myLon,station['Latitude'],station['Longitude'],theClosestOne[1])
        if  newDistance < theClosestOne[1]:
            theClosestOne = (station,newDistance) 
    return theClosestOne 

def getXMLResponse(requestURL):
    response = requests.get(requestURL)
    response.raise_for_status()
    return response.content

