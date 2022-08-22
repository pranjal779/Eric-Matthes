# THe setUp() method

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setup(self):
        """
        Create a survey and a set of responses for use in all test methods
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Hindi', 'marathi']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()

# page 257
# refer Page 259
"""
When a test case is running, Python prints one character for each unit test as it is 
completed. A passing test prints a dot, a test that results in an error prints an E, and 
a test that results in a failed assertion prints an F. This is why you’ll see a different 
number of dots and characters on the first line of output when you run your test cases. 
If a test case takes a long time to run because it contains many unit tests, you can 
watch these results to get a sense of how many tests are passing.
"""
