import json
from geopy.distance import distance
from brazilianforecastio.current import BrazilianCurrentWeather

def loadCurrentSituationOnMyLocation():
    _forecast = BrazilianCurrentWeather(coordinate=(-10.979357, -37.048752),distance_func=distance)
    _forecast.update_current()
    print(_forecast.current_situation_XML)
    print(_forecast.get_reading('weather'))
    print(_forecast.get_formated_icon_URL(_isNight=True))

def whereIsRaining(_isNight=False):
    for station in json.loads(BrazilianCurrentWeather.airport_station_json):
        statiton_current = BrazilianCurrentWeather(station_id=station['Sigla'],distance_func=distance)
        statiton_current.update_current()
        if statiton_current.get_reading('weather')=='c':
            print(statiton_current.station_id)
            print(statiton_current.get_formated_icon_URL(_isNight))
            print(statiton_current.current_situation_XML)