import threading
from forecast import BrazilianForecast

def loadCurrentSituation(lat, lng):
    """
        lat: The latitude of the forecast
        lng: The longitude of the forecast
    """
    forecast = BrazilianForecast(lat, lng)
    return forecast.update()

print (loadCurrentSituation(-10.981991, -37.053559).XMLCurrentSituationData)