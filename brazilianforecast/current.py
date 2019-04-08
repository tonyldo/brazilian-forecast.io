import xml.etree.ElementTree as ET
from brazilianforecast.station import Station
import requests


class BrazilianCurrentWeather():

    conditions_reference = {
        'pressure': 'pressao',
        'temperature': 'temperatura',
        'weather': 'tempo',
        'weather_desc': 'tempo_desc',
        'humidity': 'umidade',
        'wind_dir': 'vento_dir',
        'wind_speed': 'vento_int',
        'visibility': 'visibilidade',
        'last_time_updated': 'atualizacao',
        'station_code': 'codigo'
    }

    _CURRENT_DATA_URL = 'http://servicos.cptec.inpe.br/XML/estacao/%s/condicoesAtuais.xml'
    _ICON_URL = 'https://s%s.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/%s.png'

    def __init__(self, current_data_url=None, icon_url=None):
        self._current_data_url = self._CURRENT_DATA_URL if not current_data_url else current_data_url
        self._icon_url = self._ICON_URL if not icon_url else icon_url
        self._conditions = {}
        self._host_number_icon_Url = 0

    def set_station(self, station):
        self.station = station
        return self

    def get_station_current_conditions(self):
        return self.get_current_conditions(self.station.id)

    def get_formated_current_situation_URL(self, station_id):
        return self._current_data_url % station_id

    def validate_icon_url(self, weather_code, _isNight_sufix=None):
        resp = requests.get(self._icon_url % (
            self._host_number_icon_Url, weather_code))
        if resp.status_code != 200:
            return None
        save_resp_url = resp.url
        if _isNight_sufix is not None:
            resp = requests.get(self._icon_url % (
                self._host_number_icon_Url, weather_code+_isNight_sufix))
            if resp.status_code == 200:
                return resp.url
        return save_resp_url

    def get_formated_icon_URL(self, weather_code, _isNight=False):
        return self.validate_icon_url(weather_code, _isNight_sufix='_n' if _isNight else None)

    def get_reading(self, condition):
        return self._conditions[self.conditions_reference[condition]]

    def _update_readings(self, current_situation_XML):
        root = ET.fromstring(current_situation_XML)
        for element in root.findall("./*"):
            self._conditions[element.tag] = element.text

    def get_current_conditions(self, station_id):
        resp = requests.get(
            self.get_formated_current_situation_URL(station_id))
        if resp.status_code != 200:
            return None
        self._update_readings(resp.content)
        return self
