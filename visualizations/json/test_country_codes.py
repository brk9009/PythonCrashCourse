import unittest
from country_codes import get_country_code

class CountryCodesTest(unittest.TestCase):
    """Tests for 'country_codes.py'"""

    def test_get_country_code(self):
        country_code = get_country_code('United States')
        self.assertEqual(country_code,'us')

unittest.main()