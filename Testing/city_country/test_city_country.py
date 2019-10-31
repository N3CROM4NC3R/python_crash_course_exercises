import unittest
from city_functions import city_country

class test_city_country_function(unittest.TestCase):

    def test_city_country(self):
        """ Do location like 'Santiago, Chile' works?"""
        location = city_country('santiago','chile')
        self.assertEqual(location,'Santiago, Chile')

    def test_city_country_not_equal(self):
        """ Not equal location 'Santiago, Chile' with 'Antiago, Chile'"""
        location = city_country('santiago','chile')
        self.assertNotEqual(location,'Antiago, Chile')
