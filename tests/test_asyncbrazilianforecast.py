from aiohttp import ClientSession, ClientConnectorError
from brazilianforecast.async_current import AsyncBrazilianCurrentWeatherService
from brazilianforecast.station import Station 

async def test_current_station_condition(loop):
     try:
          async with ClientSession() as session:
               sbar_station_current_conditions = await Station('SBAR').set_weather_service(AsyncBrazilianCurrentWeatherService(session)).async_get_current_conditions()
          assert sbar_station_current_conditions.get_reading('station_code')=='SBAR'
     except ClientConnectorError:
         pass


async def test_current_station_url_symbol(loop):
    async with ClientSession() as session:
         sbar_station_current_conditions = Station('SBAR').set_weather_service(AsyncBrazilianCurrentWeatherService(session))
         sbar_station_current_conditions.weather_service._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pc</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
         assert sbar_station_current_conditions.weather_service.get_reading('station_code') == 'SBAR'
         try:
              url = await sbar_station_current_conditions.async_get_current_symbol_url()
              filename = url[url.rfind('/')+1:]
              assert 'pc' in filename
         except ClientConnectorError:
              pass
