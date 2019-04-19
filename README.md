# Brazilian Forecast

Friendly Python API for Brazilian Forecast powered by CPTEC-INPE Data (http://servicos.cptec.inpe.br/XML/) .

## Installation

You should use pip to install brazilian-forecastio.

* To install pip install brazilian-forecastio
* To remove pip uninstall brazilian-forecastio

## Requirements
* Python 3.X

## Basic Use

```
import brazilianforecast

if __name__ == "__main__":
    current_conditions = brazilianforecast.load_current(-10.979968, -37.055018)
    print(current_conditions.get_reading('temperature'))
``` 
or async call like:

```
import aiohttp
import asyncio
import brazilianforecast

async def main():
    async with aiohttp.ClientSession() as session:
        current_conditions = await brazilianforecast.async_load_current(-10.979968, -37.055018,session)
        print(current_conditions.get_reading('wind_speed'))
       
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

The ``get_reading()`` method has a few optional parameters:

* ``pressure``
* ``temperature``
* ``weather``
* ``weather_des``
* ``humidity``
* ``wind_dir``
* ``wind_speed``
* ``visibility``
* ``last_time_updated``
* ``station_code``

<figure class="video_container">
<iframe src="https://s0.cptec.inpe.br/webcptec/common/legenda.html"></iframe>
</figure>
