import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.pranjal = Employee('pranjal', 'Shukla', 65_000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.pranjal.give_raise()
        self.assertEqual(self.pranjal.annual_salary, 70000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.pranjal.give_raise(10000)
        self.assertEqual(self.pranjal.annual_salary, 75000)


if __name__ == '__main__':
    unittest.main()


""""
this error shows up if from employee file in the give_raise() amount is not set as 
an positional argument 'amount=5000'
it wont add
def test_give_custom_raise(self):
                
--->
        Test that a custom raise works correctly.
>       self.pranjal.give_raise(10000)
E       TypeError: give_raise() takes 1 positional argument but 2 were given
<---

"""
