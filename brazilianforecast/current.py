import xml.etree.ElementTree as ET
from brazilianforecast.station import Station 


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
        'last_time_updated': 'atualizacao'
    }

    _CURRENT_DATA_URL = 'http://servicos.cptec.inpe.br/XML/estacao/%s/condicoesAtuais.xml'
    _ICON_URL = 'https://s%s.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/%s.png'

    def __init__(self, station_id=None, coordinates=None, current_data_url=None, icon_url=None, async_session=None):
        self.current_data_url = self._CURRENT_DATA_URL if not current_data_url else current_data_url
        self.icon_url = self._ICON_URL if not icon_url else icon_url
        self.current_situation_XML = None
        self.request = async_session
        if self.request is None:
          import requests
          self.request=requests
        self._conditions = {}
        self.host_number_icon_Url = 0
        self.station = Station(id= station_id,coordenate= coordinates)

    def get_formated_current_situation_URL(self):
        return self.current_data_url % self.station.id

    async def async_test_icon_url(self, weather_code, _isNight_sufix=None):
          resp = await self.request.get(self.icon_url % (
                self.host_number_icon_Url, weather_code))
          if resp.status !=200:
            return None
          save_resp_url = str(resp.url)
          if _isNight_sufix is not None:
             resp = await self.request.get(self.icon_url % (self.host_number_icon_Url, weather_code+_isNight_sufix))
             if resp.status == 200:
                return str(resp.url)
          return save_resp_url
    
    async def async_get_formated_icon_URL(self, _isNight=False):
        if self.current_situation_XML is None:
            return None
        return await self.async_test_icon_url(self.get_reading('weather'), _isNight_sufix='_n' if _isNight else None)

    def test_icon_url(self, weather_code, _isNight_sufix=None):
          resp = self.request.get(self.icon_url % (
                self.host_number_icon_Url, weather_code))
          if resp.status_code !=200:
             return None
          save_resp_url = resp.url
          if _isNight_sufix is not None:
             resp = self.request.get(self.icon_url % (self.host_number_icon_Url, weather_code+_isNight_sufix))
             if resp.status_code == 200:
                return resp.url
          return save_resp_url
    
    def get_formated_icon_URL(self, _isNight=False):
        if self.current_situation_XML is None:
            return None
        return self.test_icon_url(self.get_reading('weather'), _isNight_sufix='_n' if _isNight else None)

    def get_reading(self, _condition):
        return self._conditions[self.conditions_reference[_condition]]

    def update_readings(self, _current_situation_XML=None):
        if _current_situation_XML is not None:
            self.current_situation_XML = _current_situation_XML
        root = ET.fromstring(self.current_situation_XML)
        for element in root.findall("./*"):
            self._conditions[element.tag] = element.text

    async def async_update_current(self):
        resp = await self.request.get(
            self.get_formated_current_situation_URL())
        self.current_situation_XML = await resp.text()
        self.update_readings()
        return self

    def update_current(self):
        resp = self.request.get(self.get_formated_current_situation_URL())
        self.current_situation_XML = resp.content
        self.update_readings()
        return self

