import unittest
from name_function03 import get_formatted_name_03


class NamesTestCase(unittest.TestCase):
    """Creating test case to Fail"""

    def test_first_last_name(self):
        formatted_names = get_formatted_name_03('Open', 'bejati')
        self.assertEqual(formatted_names, 'Open Bejati')


if __name__ == '__main__':
    unittest.main()


"""check page 252"""
"""
To make middle names optional, we move the parameter middle to the 
end of the parameter list in the function definition and give it an empty 
default value. We also add an {{'if' 'test'}} that builds the full name properly, 
depending on whether or not a middle name is provided

why 'if test'
I thought i need to add a if to the test case/ unit-test file
"""
