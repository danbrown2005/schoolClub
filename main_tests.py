import unittest
from io import StringIO
from unittest import mock
import sys
from main import return_grade, output_sorted_dict
from inputHandler import accept_str, accept_int


class TestInputHandler(unittest.TestCase):

    def setUp(self):
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_returnGrade_fail(self):
        result = return_grade(30, "John")
        self.assertEqual(result, "Fail")

    def test_returnGrade_pass(self):
        result = return_grade(45, "John")
        self.assertEqual(result, "Pass")

    def test_returnGrade_merit(self):
        result = return_grade(65, "John")
        self.assertEqual(result, "Merit")

    def test_returnGrade_distinction_with_alert(self):
        with mock.patch('builtins.print') as mock_print:
            result = return_grade(85, "John", alert=True)
        self.assertEqual(result, "Distinction")
        mock_print.assert_called_once_with("Distinction has been achieved by John who gained 85 marks!")

    def test_returnGrade_distinction_without_alert(self):
        with mock.patch('builtins.print') as mock_print:
            result = return_grade(85, "John", alert=False)
        self.assertEqual(result, "Distinction")
        mock_print.assert_not_called()

    def test_outputSortedDict(self):
        student_dict = {'John': 85, 'Alice': 92, 'Bob': 78}
        expected_output = "1: Name: Alice, Mark: 92 Grade: Distinction\n" \
                          "2: Name: John, Mark: 85 Grade: Distinction\n" \
                          "3: Name: Bob, Mark: 78 Grade: Distinction\n"
        output_sorted_dict(student_dict)
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_outputSortedDict_empty_dict(self):
        student_dict = {}
        expected_output = ""  # No output for an empty dictionary
        output_sorted_dict(student_dict)
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_acceptInt_valid_input(self):
        # Test with valid input within bounds
        input_values = ['5']
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            result = accept_int(prompt_message="Enter an integer: ", lower_bound=1, upper_bound=10)
        self.assertEqual(result, 5)

    def test_acceptInt_out_of_bounds(self):
        # Test with input out of bounds
        input_values = ['15', '5']
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            result = accept_int(prompt_message="Enter an integer: ", lower_bound=1, upper_bound=10)
        expected_output = "Please input a valid integer\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)
        self.assertEqual(result, 5)

    def test_acceptInt_invalid_input(self):
        # Test with invalid input (not an integer)
        input_values = ['abc', '5']
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            result = accept_int(prompt_message="Enter an integer: ")
        expected_output = "Please input a valid integer\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)
        self.assertEqual(result, 5)

    def test_acceptStr_valid_input(self):
        # Test with valid alphabetical string
        input_values = ['abc']
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            result = accept_str(prompt_message="Enter a string: ")
        self.assertEqual(result, 'abc')

    def test_acceptStr_invalid_input(self):
        # Test with invalid input (contains non-alphabetical characters)
        input_values = ['abc123', 'abc']
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            result = accept_str(prompt_message="Enter a string: ")
        expected_output = "Please input a valid alphabetical string\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)
        self.assertEqual(result, 'abc')

    def test_acceptStr_empty_string(self):
        input_values = ['', 'John']
        with mock.patch('builtins.input', side_effect=input_values):
            result = accept_str("Enter your student's name: ", "Invalid name entered")
        expected_output = "Invalid name entered\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)
        self.assertEqual(result, 'John')

    def test_acceptStr_whitespace_string(self):
        input_values = ['  ', 'John']
        with mock.patch('builtins.input', side_effect=input_values):
            result = accept_str("Enter your student's name: ", "Invalid name entered")
        expected_output = "Invalid name entered\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)
        self.assertEqual(result, 'John')


if __name__ == '__main__':
    unittest.main()
