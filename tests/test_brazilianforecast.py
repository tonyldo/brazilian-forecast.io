import pytest
import json
from xml.etree.ElementTree import ParseError
from brazilianforecast.station import Station
from brazilianforecast.current import BrazilianCurrentWeatherService
from requests.exceptions import ConnectionError

def test_station_constructor_by_id():
    station = Station(id='SBAR')
    assert station.id == 'SBAR'

def test_station_constructor_by_coordenates():
    station = Station(coordenate=(-10.379391, -37.674030))
    assert station.id == 'SBAR'
    station = Station(coordenate=(-10.350545, -54.716091))
    assert station.id == 'SBCC'
    station = Station(coordenate=(-20.156207, -41.927101))
    assert station.id == 'SBIP'
    station = Station(coordenate=(-26.393573, -49.392331))
    assert station.id == 'SBJV'

def test_station_not_found_constructor():
    with pytest.raises(ValueError):
        Station('SBARR')

def test_station_constructor_no_args():
    with pytest.raises(ValueError):
        Station()

def test_station_get_time_zone():
    sbfn_sation = Station('SBFN')
    assert sbfn_sation.get_time_zone() == 'Brazil/DeNoronha'
    airport_sation_data = json.loads(sbfn_sation.airport_station_json)
    brazil_east_stations = [station for station in airport_sation_data if station['Sigla'] in ('PA', 'AP', 'TO', 'GO', 'DF', 'SP', 'PR', 'SC', 'RS', 'RJ', 'MG', 'ES', 'BA', 'SE', 'AL','PI', 'PE', 'PB', 'RN', 'CE', 'MA')]
    for station in brazil_east_stations:
        st = Station(station['sigla'])
        assert st.get_time_zone() == 'Brazil/East'

def test_get_current_conditions_status_code_not_200():
    current = BrazilianCurrentWeatherService()
    try:
        assert not current.get_current_conditions('SBA9')
    except ConnectionError:
        pass

def test_current_XML_parser():
    current = BrazilianCurrentWeatherService()
    xml = "<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>"
    current._update_readings(xml)
    xml += ">"
    with pytest.raises(ParseError):
        current._update_readings(xml)

def test_current_get_reading():
    current = BrazilianCurrentWeatherService()
    current._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
    assert current.get_reading('temperature') == current._conditions['temperatura']
    assert current.get_reading('weather') == current._conditions['tempo']
    assert current.get_reading('pressure') == current._conditions['pressao']

def test_current_get_reading_key_error():
    current = BrazilianCurrentWeatherService()
    current._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
    with pytest.raises(KeyError):
        assert current.get_reading('temperatura')

def test_current_update():
    current = BrazilianCurrentWeatherService()
    current._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
    assert current.get_reading('temperature') == '29'
    current._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>30</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
    assert current.get_reading('temperature') == '30'

def test_current_station_condition():
    try:
        sbar_station_current_conditions = Station('SBAR').set_weather_service(BrazilianCurrentWeatherService()).get_current_conditions()
        assert sbar_station_current_conditions.get_reading('station_code') == 'SBAR'
    except ConnectionError:
        pass

def test_current_station_url_symbol():
    sbar_station_current_conditions = Station('SBAR').set_weather_service(BrazilianCurrentWeatherService())
    sbar_station_current_conditions.weather_service._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pc</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
    assert sbar_station_current_conditions.weather_service.get_reading('station_code') == 'SBAR'
    try:
        url = sbar_station_current_conditions.get_current_symbol_url()
        filename = url[url.rfind('/')+1:]
        assert 'pc' in filename
    except ConnectionError:
        pass
