import unittest
from city_functions import city_country

class test_city_country_function(unittest.TestCase):

    def test_city_country(self):
        """ Do location like 'Santiago, Chile' works?"""
        location = city_country('santiago','chile')
        self.assertEqual(location,'Santiago, Chile')

    def test_city_country_population(self):
        """ Do location like 'Santiago, Chile - 50000' works"""
        location = city_country('santiago','chile','50000')

        self.assertEqual(location,'Santiago, Chile - 50000')
