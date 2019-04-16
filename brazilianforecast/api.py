from brazilianforecast.current import BrazilianCurrentWeatherService
from brazilianforecast.async_current import AsyncBrazilianCurrentWeatherService
from brazilianforecast.station import Station

def load_current(lat,lon):
    return Station(coordenate=(lat,lon)).set_weather_service(BrazilianCurrentWeatherService()).get_current_conditions()

async def async_load_current(lat,lon,client_session):
    return await Station(coordenate=(lat,lon)).set_weather_service(AsyncBrazilianCurrentWeatherService(client_session)).async_get_current_conditions()
