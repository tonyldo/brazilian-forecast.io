from utils import closestStation
from utils import getXMLResponse

class BrazilianForecast():

    def __init__(self, lat, lon, airportStationJsonFile=None):
        self.lat = lat
        self.lon = lon
        self.closestStation =  closestStation(lat,lon)
        self.urlCurrentSituation = 'http://servicos.cptec.inpe.br/XML/estacao/%s/condicoesAtuais.xml' % (self.closestStation[0]['Sigla'])

    def update(self):
        self.XMLCurrentSituationData = getXMLResponse(self.urlCurrentSituation)
        return self
