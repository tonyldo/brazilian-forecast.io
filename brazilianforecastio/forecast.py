import json
import xml.etree.ElementTree as ET

class BrazilianForecast():

    conditions_reference = {
        'pressure': 'pressao',
        'temperature': 'temperatura',
        'weather': 'tempo',
        'weather_desc': 'tempo_desc',
        'humidity': 'umidade',
        'wind_dir': 'vento_dir',
        'wind_speed': 'vento_int',
        'visibility': 'visibilidade'
    }

    airportSationJson = """
[
  {
    "Sigla": "SBTK",
    "Aeroporto": "Tarauacá",
    "Estado": "AC",
    "Latitude": -8.15,
    "Longitude": -70.77
  },
  {
    "Sigla": "SBRB",
    "Aeroporto": "Presidente Médici",
    "Estado": "AC",
    "Latitude": -9.87,
    "Longitude": -67.9
  },
  {
    "Sigla": "SBCZ",
    "Aeroporto": "Internacional",
    "Estado": "AC",
    "Latitude": -7.58,
    "Longitude": -72.77
  },
  {
    "Sigla": "SBMO",
    "Aeroporto": "Zumbi dos Palmares",
    "Estado": "AL",
    "Latitude": -9.52,
    "Longitude": -35.78
  },
  {
    "Sigla": "SBEG",
    "Aeroporto": "Eduardo Gomes",
    "Estado": "AM",
    "Latitude": -3.03,
    "Longitude": -60.05
  },
  {
    "Sigla": "SBMN",
    "Aeroporto": "Ponta Pelada",
    "Estado": "AM",
    "Latitude": -3.13,
    "Longitude": -59.98
  },
  {
    "Sigla": "SBMY",
    "Aeroporto": "Manicoré",
    "Estado": "AM",
    "Latitude": -5.82,
    "Longitude": -61.29
  },
  {
    "Sigla": "SBTT",
    "Aeroporto": "Tabatinga",
    "Estado": "AM",
    "Latitude": -4.25,
    "Longitude": -69.93
  },
  {
    "Sigla": "SBYA",
    "Aeroporto": "Iuaretê",
    "Estado": "AM",
    "Latitude": 0.61,
    "Longitude": -69.2
  },
  {
    "Sigla": "SBUA",
    "Aeroporto": "São Gabriel da Cachoeira",
    "Estado": "AM",
    "Latitude": -0.13,
    "Longitude": -66.98
  },
  {
    "Sigla": "SBTF",
    "Aeroporto": "Tefé",
    "Estado": "AM",
    "Latitude": -3.38,
    "Longitude": -64.73
  },
  {
    "Sigla": "SBAM",
    "Aeroporto": "Amapá",
    "Estado": "AP",
    "Latitude": 2.07,
    "Longitude": -50.85
  },
  {
    "Sigla": "SBMQ",
    "Aeroporto": "Internacional",
    "Estado": "AP",
    "Latitude": -0.05,
    "Longitude": -51.11
  },
  {
    "Sigla": "SBOI",
    "Aeroporto": "Oiapoque",
    "Estado": "AP",
    "Latitude": 3.84,
    "Longitude": -51.82
  },
  {
    "Sigla": "SBLP",
    "Aeroporto": "Bom Jesus da Lapa",
    "Estado": "BA",
    "Latitude": -13.25,
    "Longitude": -43.41
  },
  {
    "Sigla": "SBCV",
    "Aeroporto": "Caravelas",
    "Estado": "BA",
    "Latitude": -17.65,
    "Longitude": -39.25
  },
  {
    "Sigla": "SBIL",
    "Aeroporto": "Jorge Amado",
    "Estado": "BA",
    "Latitude": -14.8,
    "Longitude": -39.02
  },
  {
    "Sigla": "SBLE",
    "Aeroporto": "Chapada Diamantina",
    "Estado": "BA",
    "Latitude": -12.48,
    "Longitude": -41.28
  },
  {
    "Sigla": "SBUF",
    "Aeroporto": "Paulo Afonso",
    "Estado": "BA",
    "Latitude": -9.36,
    "Longitude": -38.21
  },
  {
    "Sigla": "SBPS",
    "Aeroporto": "Porto Seguro",
    "Estado": "BA",
    "Latitude": -16.44,
    "Longitude": -39.07
  },
  {
    "Sigla": "SBSV",
    "Aeroporto": "Dep. Luís Eduardo Magalhães",
    "Estado": "BA",
    "Latitude": -12.91,
    "Longitude": -38.33
  },
  {
    "Sigla": "SBQV",
    "Aeroporto": "Vitória da Conquista",
    "Estado": "BA",
    "Latitude": -14.89,
    "Longitude": -40.8
  },
  {
    "Sigla": "SBFZ",
    "Aeroporto": "Pinto Martins",
    "Estado": "CE",
    "Latitude": -3.77,
    "Longitude": -38.52
  },
  {
    "Sigla": "SBJU",
    "Aeroporto": "Cariri",
    "Estado": "CE",
    "Latitude": -7.22,
    "Longitude": -39.27
  },
  {
    "Sigla": "SBBR",
    "Aeroporto": "Juscelino Kubitschek",
    "Estado": "DF",
    "Latitude": -15.87,
    "Longitude": -47.92
  },
  {
    "Sigla": "SBVT",
    "Aeroporto": "Eurico Aguiar Salles",
    "Estado": "ES",
    "Latitude": -20.25,
    "Longitude": -40.28
  },
  {
    "Sigla": "SBAN",
    "Aeroporto": "Anápolis",
    "Estado": "GO",
    "Latitude": -16.24,
    "Longitude": -48.97
  },
  {
    "Sigla": "SBGO",
    "Aeroporto": "Santa Genoveva",
    "Estado": "GO",
    "Latitude": -16.67,
    "Longitude": -49.26
  },
  {
    "Sigla": "SBCI",
    "Aeroporto": "Carolina",
    "Estado": "MA",
    "Latitude": -7.33,
    "Longitude": -47.43
  },
  {
    "Sigla": "SBIZ",
    "Aeroporto": "Imperatriz",
    "Estado": "MA",
    "Latitude": -5.54,
    "Longitude": -47.48
  },
  {
    "Sigla": "SBSL",
    "Aeroporto": "Mar. Cunha Machado",
    "Estado": "MA",
    "Latitude": -2.53,
    "Longitude": -44.3
  },
  {
    "Sigla": "SBAX",
    "Aeroporto": "Araxá",
    "Estado": "MG",
    "Latitude": -19.57,
    "Longitude": -46.97
  },
  {
    "Sigla": "SBPR",
    "Aeroporto": "Carlos Prates",
    "Estado": "MG",
    "Latitude": -19.9,
    "Longitude": -43.98
  },
  {
    "Sigla": "SBBQ",
    "Aeroporto": "Barbacena",
    "Estado": "MG",
    "Latitude": -21.24,
    "Longitude": -43.78
  },
  {
    "Sigla": "SBBH",
    "Aeroporto": "Pampulha",
    "Estado": "MG",
    "Latitude": -19.85,
    "Longitude": -43.95
  },
  {
    "Sigla": "SBCF",
    "Aeroporto": "Tancredo Neves",
    "Estado": "MG",
    "Latitude": -19.62,
    "Longitude": -43.97
  },
  {
    "Sigla": "SBPC",
    "Aeroporto": "Poços de Caldas",
    "Estado": "MG",
    "Latitude": -21.83,
    "Longitude": -46.55
  },
  {
    "Sigla": "SBUR",
    "Aeroporto": "Uberaba",
    "Estado": "MG",
    "Latitude": -19.75,
    "Longitude": -47.97
  },
  {
    "Sigla": "SBUL",
    "Aeroporto": "Uberlândia",
    "Estado": "MG",
    "Latitude": -18.88,
    "Longitude": -48.22
  },
  {
    "Sigla": "SBIP",
    "Aeroporto": "Ipatinga",
    "Estado": "MG",
    "Latitude": -19.47,
    "Longitude": -42.48
  },
  {
    "Sigla": "SBJF",
    "Aeroporto": "Francisco de Assis",
    "Estado": "MG",
    "Latitude": -21.77,
    "Longitude": -43.36
  },
  {
    "Sigla": "SBMK",
    "Aeroporto": "Montes Claros",
    "Estado": "MG",
    "Latitude": -16.69,
    "Longitude": -43.84
  },
  {
    "Sigla": "SBVG",
    "Aeroporto": "Varginha",
    "Estado": "MG",
    "Latitude": -21.58,
    "Longitude": -45.47
  },
  {
    "Sigla": "SBGV",
    "Aeroporto": "Gov. Valadares",
    "Estado": "MG",
    "Latitude": -18.88,
    "Longitude": -41.98
  },
  {
    "Sigla": "SBCG",
    "Aeroporto": "Internacional",
    "Estado": "MS",
    "Latitude": -20.47,
    "Longitude": -54.67
  },
  {
    "Sigla": "SBCR",
    "Aeroporto": "Corumbá",
    "Estado": "MS",
    "Latitude": -19,
    "Longitude": -57.67
  },
  {
    "Sigla": "SBPP",
    "Aeroporto": "Internacional",
    "Estado": "MS",
    "Latitude": -22.55,
    "Longitude": -55.7
  },
  {
    "Sigla": "SBAT",
    "Aeroporto": "Alta Floresta",
    "Estado": "MT",
    "Latitude": -9.85,
    "Longitude": -56.1
  },
  {
    "Sigla": "SBBW",
    "Aeroporto": "Barra do Garças",
    "Estado": "MT",
    "Latitude": -15.85,
    "Longitude": -52.38
  },
  {
    "Sigla": "SBCY",
    "Aeroporto": "Marechal Rondon",
    "Estado": "MT",
    "Latitude": -15.65,
    "Longitude": -56.12
  },
  {
    "Sigla": "SBHT",
    "Aeroporto": "Altamira",
    "Estado": "PA",
    "Latitude": -3.21,
    "Longitude": -52.21
  },
  {
    "Sigla": "SBBE",
    "Aeroporto": "Val-de-Cans",
    "Estado": "PA",
    "Latitude": -1.4,
    "Longitude": -48.45
  },
  {
    "Sigla": "SBIH",
    "Aeroporto": "Itaituba",
    "Estado": "PA",
    "Latitude": -4.24,
    "Longitude": -56
  },
  {
    "Sigla": "SBEK",
    "Aeroporto": "Jacareacanga",
    "Estado": "PA",
    "Latitude": -6.24,
    "Longitude": -57.73
  },
  {
    "Sigla": "SBMA",
    "Aeroporto": "Marabá",
    "Estado": "PA",
    "Latitude": -5.37,
    "Longitude": -49.13
  },
  {
    "Sigla": "SBCC",
    "Aeroporto": "Cachimbó",
    "Estado": "PA",
    "Latitude": -9.33,
    "Longitude": -54.97
  },
  {
    "Sigla": "SBTB",
    "Aeroporto": "Trombetas",
    "Estado": "PA",
    "Latitude": -1.48,
    "Longitude": -56.38
  },
  {
    "Sigla": "SBCJ",
    "Aeroporto": "Carajás",
    "Estado": "PA",
    "Latitude": -6.12,
    "Longitude": -50
  },
  {
    "Sigla": "SBSN",
    "Aeroporto": "Santarém",
    "Estado": "PA",
    "Latitude": -2.42,
    "Longitude": -54.78
  },
  {
    "Sigla": "SBTU",
    "Aeroporto": "Tucuruí",
    "Estado": "PA",
    "Latitude": -3.76,
    "Longitude": -49.67
  },
  {
    "Sigla": "SBAA",
    "Aeroporto": "Conceição do Araguaia",
    "Estado": "PA",
    "Latitude": -8.26,
    "Longitude": -49.26
  },
  {
    "Sigla": "SBKG",
    "Aeroporto": "Pres. João Suassuna",
    "Estado": "PB",
    "Latitude": -7.23,
    "Longitude": -35.9
  },
  {
    "Sigla": "SBJP",
    "Aeroporto": "Pres. Castro Pinto",
    "Estado": "PB",
    "Latitude": -7.1,
    "Longitude": -34.85
  },
  {
    "Sigla": "SBFN",
    "Aeroporto": "Fernando de Noronha",
    "Estado": "PE",
    "Latitude": -3.85,
    "Longitude": -32.42
  },
  {
    "Sigla": "SBRF",
    "Aeroporto": "Guararapes",
    "Estado": "PE",
    "Latitude": -8.12,
    "Longitude": -34.92
  },
  {
    "Sigla": "SBPL",
    "Aeroporto": "Sen. Nilo Coelho",
    "Estado": "PE",
    "Latitude": -9.37,
    "Longitude": -40.55
  },
  {
    "Sigla": "SBPB",
    "Aeroporto": "Dr. João Silva Filho",
    "Estado": "PI",
    "Latitude": -2.88,
    "Longitude": -41.72
  },
  {
    "Sigla": "SBTE",
    "Aeroporto": "Sen. Petrônio Portella",
    "Estado": "PI",
    "Latitude": -5.05,
    "Longitude": -42.82
  },
  {
    "Sigla": "SBLO",
    "Aeroporto": "Londrina",
    "Estado": "PR",
    "Latitude": -23.32,
    "Longitude": -51.14
  },
  {
    "Sigla": "SBFI",
    "Aeroporto": "Cataratas",
    "Estado": "PR",
    "Latitude": -25.6,
    "Longitude": -54.48
  },
  {
    "Sigla": "SBBI",
    "Aeroporto": "Bacacheri",
    "Estado": "PR",
    "Latitude": -25.45,
    "Longitude": -49.23
  },
  {
    "Sigla": "SBCT",
    "Aeroporto": "Afonso Pena",
    "Estado": "PR",
    "Latitude": -25.52,
    "Longitude": -49.17
  },
  {
    "Sigla": "SBMG",
    "Aeroporto": "Silvio Name Junior",
    "Estado": "PR",
    "Latitude": -23.48,
    "Longitude": -52.01
  },
  {
    "Sigla": "SBCB",
    "Aeroporto": "Cabo Frio",
    "Estado": "RJ",
    "Latitude": -22.92,
    "Longitude": -42.08
  },
  {
    "Sigla": "SBAF",
    "Aeroporto": "Afonsos",
    "Estado": "RJ",
    "Latitude": -22.88,
    "Longitude": -43.38
  },
  {
    "Sigla": "SBGL",
    "Aeroporto": "Galeão",
    "Estado": "RJ",
    "Latitude": -22.8,
    "Longitude": -43.25
  },
  {
    "Sigla": "SBJR",
    "Aeroporto": "Jacarepaguá",
    "Estado": "RJ",
    "Latitude": -22.99,
    "Longitude": -43.37
  },
  {
    "Sigla": "SBRJ",
    "Aeroporto": "Santos Dumont",
    "Estado": "RJ",
    "Latitude": -22.9,
    "Longitude": -43.15
  },
  {
    "Sigla": "SBSC",
    "Aeroporto": "Santa Cruz",
    "Estado": "RJ",
    "Latitude": -22.93,
    "Longitude": -43.72
  },
  {
    "Sigla": "SBME",
    "Aeroporto": "Macaé",
    "Estado": "RJ",
    "Latitude": -22.34,
    "Longitude": -41.75
  },
  {
    "Sigla": "SBES",
    "Aeroporto": "S. Pedro da Aldeia",
    "Estado": "RJ",
    "Latitude": -22.82,
    "Longitude": -42.09
  },
  {
    "Sigla": "SBCP",
    "Aeroporto": "Bartolomeu Lysandro",
    "Estado": "RJ",
    "Latitude": -21.74,
    "Longitude": -41.33
  },
  {
    "Sigla": "SBMS",
    "Aeroporto": "Dix-Sept Rosado",
    "Estado": "RN",
    "Latitude": -5.2,
    "Longitude": -37.37
  },
  {
    "Sigla": "SBNT",
    "Aeroporto": "Augusto Severo",
    "Estado": "RN",
    "Latitude": -5.91,
    "Longitude": -35.23
  },
  {
    "Sigla": "SBGM",
    "Aeroporto": "Guajará Mirim",
    "Estado": "RO",
    "Latitude": -10.78,
    "Longitude": -65.27
  },
  {
    "Sigla": "SBVH",
    "Aeroporto": "Brigadeiro Camarão",
    "Estado": "RO",
    "Latitude": -12.69,
    "Longitude": -60.11
  },
  {
    "Sigla": "SBPV",
    "Aeroporto": "Gov. Jorge Teixeira de Oliveira",
    "Estado": "RO",
    "Latitude": -8.7,
    "Longitude": -63.9
  },
  {
    "Sigla": "SBBV",
    "Aeroporto": "Boa Vista",
    "Estado": "RR",
    "Latitude": 2.84,
    "Longitude": -60.68
  },
  {
    "Sigla": "SBBG",
    "Aeroporto": "Bagé",
    "Estado": "RS",
    "Latitude": -31.39,
    "Longitude": -54.1
  },
  {
    "Sigla": "SBSM",
    "Aeroporto": "Santa Maria",
    "Estado": "RS",
    "Latitude": -29.7,
    "Longitude": -53.68
  },
  {
    "Sigla": "SBPA",
    "Aeroporto": "Salgado Filho",
    "Estado": "RS",
    "Latitude": -29.99,
    "Longitude": -51.17
  },
  {
    "Sigla": "SBPK",
    "Aeroporto": "Pelotas",
    "Estado": "RS",
    "Latitude": -31.8,
    "Longitude": -52.41
  },
  {
    "Sigla": "SBCO",
    "Aeroporto": "Canoas",
    "Estado": "RS",
    "Latitude": -29.93,
    "Longitude": -51.13
  },
  {
    "Sigla": "SBUG",
    "Aeroporto": "Rubem Berta",
    "Estado": "RS",
    "Latitude": -29.77,
    "Longitude": -57.03
  },
  {
    "Sigla": "SBCH",
    "Aeroporto": "Chapecó",
    "Estado": "SC",
    "Latitude": -27.14,
    "Longitude": -52.66
  },
  {
    "Sigla": "SBCM",
    "Aeroporto": "Forquilinha",
    "Estado": "SC",
    "Latitude": -28.72,
    "Longitude": -49.42
  },
  {
    "Sigla": "SBFL",
    "Aeroporto": "Hercílio Luz",
    "Estado": "SC",
    "Latitude": -27.67,
    "Longitude": -48.55
  },
  {
    "Sigla": "SBJV",
    "Aeroporto": "Lauro Carneiro de Loyola",
    "Estado": "SC",
    "Latitude": -26.22,
    "Longitude": -48.8
  },
  {
    "Sigla": "SBNF",
    "Aeroporto": "Min. Victor Konder",
    "Estado": "SC",
    "Latitude": -26.87,
    "Longitude": -48.63
  },
  {
    "Sigla": "SBAR",
    "Aeroporto": "Santa Maria",
    "Estado": "SE",
    "Latitude": -10.99,
    "Longitude": -37.07
  },
  {
    "Sigla": "SBAU",
    "Aeroporto": "Araçatuba",
    "Estado": "SP",
    "Latitude": -21.2,
    "Longitude": -50.43
  },
  {
    "Sigla": "SBBU",
    "Aeroporto": "Bauru",
    "Estado": "SP",
    "Latitude": -22.34,
    "Longitude": -49.05
  },
  {
    "Sigla": "SBKP",
    "Aeroporto": "Viracopos",
    "Estado": "SP",
    "Latitude": -23,
    "Longitude": -47.13
  },
  {
    "Sigla": "SBDN",
    "Aeroporto": "Pres. Prudente",
    "Estado": "SP",
    "Latitude": -22.11,
    "Longitude": -51.38
  },
  {
    "Sigla": "SBRP",
    "Aeroporto": "Leite Lopes",
    "Estado": "SP",
    "Latitude": -21.12,
    "Longitude": -47.77
  },
  {
    "Sigla": "SBSR",
    "Aeroporto": "S. J. do Rio Preto",
    "Estado": "SP",
    "Latitude": -20.8,
    "Longitude": -49.4
  },
  {
    "Sigla": "SBYS",
    "Aeroporto": "Fontenelle",
    "Estado": "SP",
    "Latitude": -21.98,
    "Longitude": -47.34
  },
  {
    "Sigla": "SBST",
    "Aeroporto": "Base Aérea",
    "Estado": "SP",
    "Latitude": -23.92,
    "Longitude": -46.28
  },
  {
    "Sigla": "SBGP",
    "Aeroporto": "Gavião Peixoto",
    "Estado": "SP",
    "Latitude": -21.77,
    "Longitude": -48.4
  },
  {
    "Sigla": "SBGW",
    "Aeroporto": "Guaratinguetá",
    "Estado": "SP",
    "Latitude": -22.79,
    "Longitude": -45.2
  },
  {
    "Sigla": "SBGR",
    "Aeroporto": "Guarulhos",
    "Estado": "SP",
    "Latitude": -23.44,
    "Longitude": -46.47
  },
  {
    "Sigla": "SBSJ",
    "Aeroporto": "São J. dos Campos",
    "Estado": "SP",
    "Latitude": -23.22,
    "Longitude": -45.87
  },
  {
    "Sigla": "SBMT",
    "Aeroporto": "Campo de Marte",
    "Estado": "SP",
    "Latitude": -23.51,
    "Longitude": -46.63
  },
  {
    "Sigla": "SBSP",
    "Aeroporto": "Congonhas",
    "Estado": "SP",
    "Latitude": -23.62,
    "Longitude": -46.65
  },
  {
    "Sigla": "SBTA",
    "Aeroporto": "Taubaté",
    "Estado": "SP",
    "Latitude": -23.03,
    "Longitude": -45.5
  },
  {
    "Sigla": "SBPJ",
    "Aeroporto": "Palmas",
    "Estado": "TO",
    "Latitude": -10.28,
    "Longitude": -48.35
  },
  {
    "Sigla": "SBPN",
    "Aeroporto": "Porto Nacional",
    "Estado": "TO",
    "Latitude": -10.72,
    "Longitude": -48.4
  }
] """

    _CURRENT_DATA_URL = 'http://servicos.cptec.inpe.br/XML/estacao/%s/condicoesAtuais.xml'
    _ICON_URL = 'https://s%s.cptec.inpe.br/webcptec/common/assets/images/icones/tempo/icones-grandes/%s.png'

    def __init__(self, station_id=None, coordinate=None, distanceFunc=None, current_data_url=None, icon_url=None, request=None):
        self.coordinate = coordinate
        self.station_id = station_id
        self.distanceFunc = distanceFunc
        self.current_data_url = current_data_url
        self.icon_url = icon_url
        self.XMLCurrentSituationData = None
        self.request = request
        self.conditions = {}
        self.hostNumberForIconUrl = 0

    def isNigth(self):
      from datetime import datetime
      return datetime.strptime(self.conditions['atualizacao'], '%d/%m/%Y %H:%M:%S').hour > 18    

    def get_formated_current_situation_URL(self):
        if self.current_data_url is None:
          self.current_data_url = self._CURRENT_DATA_URL
        return self.current_data_url%self.getStationId()

    def get_formated_icon_URL(self):
        if self.XMLCurrentSituationData is None:
          self.update()
        if self.icon_url is None:
           self.icon_url = self._ICON_URL
        weather_code = self.conditions['tempo']
        if self.isNigth():
           weather_code += '_n' 
        return self.icon_url%(self.hostNumberForIconUrl, weather_code)

    def condition_readings(self,_condition):
       return self.conditions[self.conditions_reference[_condition]]

    def updateConditions(self, _XMLCurrentSituationData=None):
      if _XMLCurrentSituationData is not None:
        self.XMLCurrentSituationData = _XMLCurrentSituationData
      root = ET.fromstring(self.XMLCurrentSituationData)
      for element in root.findall("./*"):
        self.conditions[element.tag] = element.text

    def update(self):
      self.XMLCurrentSituationData = self.getXMLResponse()
      self.updateConditions()
      return self

    def closestStation(self):
      airportSationData = json.loads(self.airportSationJson)
      theClosestOne = airportSationData[0], self.distanceFunc(
            self.coordinate, (airportSationData[0]['Latitude'], airportSationData[0]['Longitude']))
      for station in airportSationData:
        newDistance = self.distanceFunc(
          self.coordinate, (station['Latitude'], station['Longitude']))
        if (newDistance<theClosestOne[1]):
          theClosestOne = (station, newDistance)
      
      return theClosestOne

    def getStationId(self):
        if self.station_id is None:
          self.station_id = self.closestStation()[0]['Sigla']
        return self.station_id

    def getXMLResponse(self):
      if self.request is None:
        import requests
        self.request = requests
      response = self.request.get(self.get_formated_current_situation_URL())
      return response.content
