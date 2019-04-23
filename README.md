# Brazilian Forecast

Friendly Python API for Brazilian Forecast powered by CPTEC-INPE Data (http://servicos.cptec.inpe.br/XML/) .

## Installation

You should use pip to install brazilian-forecastio.

* To install pip install brazilian-forecastio
* To remove pip uninstall brazilian-forecastio

## Requirements
* Python 3.X

## Basic Use

* The basic use is call the ``load_current()`` method passing latitude and longitude.

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
        current_conditions = await brazilianforecast.async_load_current(-10.979968, -37.055018, session)
        print(current_conditions.get_reading('wind_speed'))
       
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

The ``get_reading()`` method accept the follows conditions:

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


weather code and descriptions... for now, in portuguese

| Sigla | Descrição                          |
|-------|------------------------------------|
| ec    | Encoberto com Chuvas Isoladas      |
| ci    | Chuvas Isoladas                    |
| c     | Chuva                              |
| in    | Instável                           |
| pp    | Poss. de Pancadas de Chuva         |
| cm    | Chuva pela Manhã                   |
| cn    | Chuva a Noite                      |
| pt    | Pancadas de Chuva a Tarde          |
| pm    | Pancadas de Chuva pela Manhã       |
| np    | Nublado e Pancadas de Chuva        |
| pc    | Pancadas de Chuva                  |
| pn    | Parcialmente Nublado               |
| cv    | Chuvisco                           |
| ch    | Chuvoso                            |
| t     | Tempestade                         |
| ps    | Predomínio de Sol                  |
| e     | Encoberto                          |
| n     | Nublado                            |
| cl    | Céu Claro                          |
| nv    | Nevoeiro                           |
| g     | Geada                              |
| ne    | Neve                               |
| nd    | Não Definido                       |
| pnt   | Pancadas de Chuva a Noite          |
| psc   | Possibilidade de Chuva             |
| pcm   | Possibilidade de Chuva pela Manhã  |
| pct   | Possibilidade de Chuva a Tarde     |
| pcn   | Possibilidade de Chuva a Noite     |
| npt   | Nublado com Pancadas a Tarde       |
| npn   | Nublado com Pancadas a Noite       |
| ncn   | Nublado com Poss. de Chuva a Noite |
| nct   | Nublado com Poss. de Chuva a Tarde |
| ncm   | Nubl. c/ Poss. de Chuva pela Manhã |
| npm   | Nublado com Pancadas pela Manhã    |
| npp   | Nublado com Possibilidade de Chuva |
| vn    | Variação de Nebulosidade           |
| ct    | Chuva a Tarde                      |
| ppn   | Poss. de Panc. de Chuva a Noite    |
| ppt   | Poss. de Panc. de Chuva a Tarde    |
| ppm   | Poss. de Panc. de Chuva pela Manhã |

