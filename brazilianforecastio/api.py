import requests
import threading

from utils import closestStation
from utils import loadStationAirportJSON


def load_forecast(lat, lng, callback=None):
    """
        This function builds the request url and loads some or all of the
        needed json depending on lazy is True
        inLat:  The latitude of the forecast
        inLong: The longitude of the forecast
        callback: function to invoke when the api get the response from CPTEC
    """
    closestStationCode = closestStation(lat, lng)[0]['Sigla']
    url = 'http://servicos.cptec.inpe.br/XML/estacao/%s/condicoesAtuais.xml' % (closestStationCode)
    return manual(url, callback=callback)


def manual(requestURL, callback=None):
    """
        This function is used by load_forecast OR by users to manually
        construct the URL for an API call.
    """
    if callback is None:
        return get_forecast(requestURL)
    else:
        thread = threading.Thread(target=load_async,args=(requestURL, callback))
        thread.start()


def get_forecast(requestURL):
    brazilianforecastio_reponse = requests.get(requestURL)
    brazilianforecastio_reponse.raise_for_status()
    xml = brazilianforecastio_reponse.content
    return xml


def load_async(url, callback):
    callback(get_forecast(url))


print (load_forecast(-9.905635, -36.061070,))