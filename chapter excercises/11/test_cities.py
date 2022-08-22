import unittest

from city_function import city_country


class CitiesTestCase(unittest.TestCase):
    """Creating tests for cites function"""

    def test_city_country(self):
        jabalpur_home = city_country('jabalpur', 'home')
        self.assertEqual(jabalpur_home, 'Jabalpur Home')


if __name__ == '__main__':
    unittest.main()
