import unittest
from city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Test functions is 'city_functions.py'"""

    def test_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country = get_city_country('santiago', 'chile', 'population=5000000')
        self.assertEqual(city_country, 'Santiago, Chile - Population=5000000')

unittest.main()
