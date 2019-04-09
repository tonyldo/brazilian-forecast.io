from aiohttp import ClientSession
from brazilianforecast.async_current import AsyncBrazilianCurrentWeather

async def test_test_user(loop):
    async with ClientSession() as session:
         current = AsyncBrazilianCurrentWeather()
         current = await current.async_update_current(session, 'SBAR')
    assert current.get_reading('station_code')=='SBAR'