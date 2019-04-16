from brazilianforecast.current import BrazilianCurrentWeatherService


class AsyncBrazilianCurrentWeatherService(BrazilianCurrentWeatherService):

    def __init__(self, async_session):
        self.async_session=async_session
        BrazilianCurrentWeatherService.__init__(self)

    async def async_test_icon_url(self, weather_code, _isNight_sufix=None):
        resp = await self.async_session.get(self._icon_url % (
            self._host_number_icon_Url, weather_code))
        if resp.status != 200:
            return None
        save_resp_url = str(resp.url)
        if _isNight_sufix is not None:
            resp = await self.async_session.get(self._icon_url % (self._host_number_icon_Url, weather_code+_isNight_sufix))
            if resp.status == 200:
                return str(resp.url)
        return save_resp_url

    async def async_get_formated_icon_URL(self,weather_code, _isNight=False):
        return await self.async_test_icon_url(weather_code, _isNight_sufix='_n' if _isNight else None)

    async def async_get_current_conditions(self, station_id):
        resp = await self.async_session.get(
            self.get_formated_current_situation_URL(station_id))
        if resp.status != 200:
            return None    
        self._update_readings(await resp.text())
        return self
