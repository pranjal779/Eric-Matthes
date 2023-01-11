import unittest
from name_function02 import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Creating test case to Fail"""

    def test_first_last_name(self):
        formatted_names = get_formatted_name('Open', 'bejati', 'krrwalo')
        self.assertEqual(formatted_names, 'Open Bejati krrwalo')


# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    unittest.main()


"""
Page 251
save time by adding main function
by  having class object.main and select the expression 'expr'
among the options

self.assert every objects needs to be correct otherwise test will fail here th middle name,
"""
