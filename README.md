*******************
# Brazilian Forecast
*******************

Friendly Python API for Brazilian Forecast powered by CPTE-INPE Data (http://servicos.cptec.inpe.br/XML/) .

## Installation

You should use pip to install brazilian-forecastio.

* To install pip install brazilian-forecastio
* To remove pip uninstall pbrazilian-forecastio

## Requirements
* Python 3.X

## Basic Use

```
import brazilianforecast

current_conditions = brazilianforecast.load_current(-10.979968, -37.055018)
current_conditions.get_reading('weather')
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