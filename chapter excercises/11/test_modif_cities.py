import unittest

from modif_city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py' """

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, ' Santiago, Chile')

    def test_city_country_population(self):
        """Can I include a population argument?"""
        santiago_chile = city_country('santiago', 'chile', population=5_000_000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
