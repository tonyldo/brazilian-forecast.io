import aiohttp
import asyncio
import brazilianforecast

async def main():
    async with aiohttp.ClientSession() as session:
        current_conditions = await brazilianforecast.async_load_current(-10.979968, -37.055018,session)
        print(current_conditions.get_reading('wind_speed'))
        symbol_url = await current_conditions.async_get_formated_icon_URL(current_conditions.get_reading('weather'))
        print(symbol_url)
       
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
