import unittest
from xml.etree.ElementTree import ParseError
from brazilianforecast.station import Station
from brazilianforecast.current import BrazilianCurrentWeather
from requests.exceptions import ConnectionError


class TestStation(unittest.TestCase):

    def test_station_constructor_by_id(self):
        station = Station(id='SBAR')
        self.assertEqual(station.id, 'SBAR')

    def test_station_constructor_by_coordenates(self):
        station = Station(coordenate=(-10.379391, -37.674030))
        self.assertEqual(station.id, 'SBAR')

        station = Station(coordenate=(-10.350545, -54.716091))
        self.assertEqual(station.id, 'SBCC')

        station = Station(coordenate=(-20.156207, -41.927101))
        self.assertEqual(station.id, 'SBIP')

        station = Station(coordenate=(-26.393573, -49.392331))
        self.assertEqual(station.id, 'SBJV')

    def test_station_not_found_constructor(self):
        with self.assertRaises(ValueError):
            Station('SBARR')

    def test_station_constructor_no_args(self):
        with self.assertRaises(ValueError):
            Station()


class CurrentWeatherTests(unittest.TestCase):

    def test_get_current_conditions(self):
        current = BrazilianCurrentWeather()
        try:
            self.assertIsNone(current.get_current_conditions('SBA9'))
        except ConnectionError:
            self.assertTrue(True)

    def test_current_XML_parser(self):
        current = BrazilianCurrentWeather()
        xml = "<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>"
        current._update_readings(xml)
        xml += ">"
        with self.assertRaises(ParseError):
            current._update_readings(xml)

    def test_current_get_reading(self):
        current = BrazilianCurrentWeather()
        current._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
        self.assertEqual(current.get_reading('temperature'),
                         current._conditions['temperatura'])
        self.assertEqual(current.get_reading('weather'),
                         current._conditions['tempo'])
        self.assertEqual(current.get_reading('pressure'),
                         current._conditions['pressao'])

    def test_current_update(self):
        current = BrazilianCurrentWeather()
        current._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>29</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
        self.assertEqual(current.get_reading('temperature'), '29')
        current._update_readings("<?xml version='1.0' encoding='ISO-8859-1'?><metar><codigo>SBAR</codigo><atualizacao>07/04/2019 13:00:00</atualizacao><pressao>1014</pressao><temperatura>30</temperatura><tempo>pn</tempo><tempo_desc>Parcialmente Nublado</tempo_desc><umidade>62</umidade><vento_dir>110</vento_dir><vento_int>20</vento_int><visibilidade>>10000</visibilidade></metar>")
        self.assertEqual(current.get_reading('temperature'), '30')

    def test_current_station_condition(self):
        try:
            sbar_station = BrazilianCurrentWeather().set_station(
                Station('SBAR')).get_station_current_conditions()
            self.assertEqual(sbar_station.get_reading('station_code'), 'SBAR')
        except ConnectionError:
            self.assertTrue(True)
