from geopy.distance import distance
from brazilianforecastio.forecast import BrazilianForecast

def loadCurrentSituation(_coordinate,_distance):
    _forecast = BrazilianForecast(coordinate=_coordinate,distanceFunc=_distance)
    return _forecast.update_currently()

currently = loadCurrentSituation((-10.979357, -37.048752),distance)
print(currently.current_situation_XML)
print(currently.get_reading('weather'))
print(currently.get_formated_icon_URL(_isNight=False))