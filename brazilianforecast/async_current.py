from brazilianforecast.current import BrazilianCurrentWeather


class AsyncBrazilianCurrentWeather(BrazilianCurrentWeather):

    async def async_test_icon_url(self, async_session, weather_code, _isNight_sufix=None):
        resp = await async_session.requests.get(self._icon_url % (
            self._host_number_icon_Url, weather_code))
        if resp.status != 200:
            return None
        save_resp_url = str(resp.url)
        if _isNight_sufix is not None:
            resp = await async_session.requests.get(self._icon_url % (self._host_number_icon_Url, weather_code+_isNight_sufix))
            if resp.status == 200:
                return str(resp.url)
        return save_resp_url

    async def async_get_formated_icon_URL(self, async_session, _isNight=False):
        return await self.async_test_icon_url(async_session, self.get_reading('weather'), _isNight_sufix='_n' if _isNight else None)

    async def async_update_current(self, async_session, station_id):
        resp = await async_session.requests.get(
            self.get_formated_current_situation_URL(station_id))
        self._update_readings(await resp.text())
        return self
