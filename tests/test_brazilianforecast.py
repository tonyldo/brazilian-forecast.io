import unittest
from brazilianforecast.station import Station

class TestStation(unittest.TestCase):

   def test_station_constructor_by_id(self):
       station = Station(id='SBAR')
       self.assertEqual(station.id,'SBAR')

   def test_station_constructor_by_coordenates(self):
       station = Station(coordenate=(-10.379391, -37.674030))
       self.assertEqual(station.id,'SBAR')

       station = Station(coordenate=(-10.350545, -54.716091))
       self.assertEqual(station.id,'SBCC')

       station = Station(coordenate=(-20.156207, -41.927101))
       self.assertEqual(station.id,'SBIP')

       station = Station(coordenate=(-26.393573, -49.392331))
       self.assertEqual(station.id,'SBJV')

   def test_station_not_found_constructor(self):
       with self.assertRaises(ValueError):
           Station('SBARR')

   def test_station_constructor_no_args(self):
       with self.assertRaises(ValueError):
           Station()
