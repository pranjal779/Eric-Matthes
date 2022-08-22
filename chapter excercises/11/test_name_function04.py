import unittest
from name_function03 import get_formatted_name_03


class NamesTestCase(unittest.TestCase):
    """Adding new Tests"""

    def test_first_last_name(self):
        formatted_names = get_formatted_name_03('Open', 'bejati')
        self.assertEqual(formatted_names, 'Open Bejati')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name_03(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
