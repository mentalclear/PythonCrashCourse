import unittest
from city_functions import formatted_city_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        """ Make sure that the function return exepcted fromat 
            inputs like: 'santiago', 'chile'
        """
        formatted_result = formatted_city_country('santiago', 'chile')
        self.assertEquals(formatted_result, 'Santiago, Chile')

    def test_city_country_population(self):
        """ Make sure that the function return expected fromat 
            inputs like: 'santiago', 'chile', 5000000
        """
        formatted_result = formatted_city_country('santiago', 'chile', 5000000)
        self.assertEquals(formatted_result, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()    
    