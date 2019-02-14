from geopy.distance import distance
import requests
import current

def loadCurrentSituation(_coordinate,_distance):
    _forecast = current.BrazilianCurrentWeather(coordinate=_coordinate,distance_func=_distance,web_session=requests)
    return _forecast.update_currently()


currently = loadCurrentSituation((-10.979357, -37.048752),distance)
print(currently.current_situation_XML)
print(currently.get_reading('weather'))
currently.host_number_icon_Url = 0
print(currently.get_formated_icon_URL(_isNight=True))