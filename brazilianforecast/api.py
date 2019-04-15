from brazilianforecast.current import BrazilianCurrentWeatherService
from brazilianforecast.station import Station

def load_current(lat,lon):
    return Station(coordenate=(lat,lon)).set_weather_service(BrazilianCurrentWeatherService()).get_current_conditions()
