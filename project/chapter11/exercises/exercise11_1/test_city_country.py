import unittest
from city_functions import formatted_city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        """ Make sure that the function return exepcted fromat 
            inputs like: 'santiago', 'chile'
        """
        formatted_result = formatted_city_country('santiago', 'chile')
        self.assertEquals(formatted_result, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()    
    