# Author: INSERT CHRIS, Ricardo Cousins (cousinsr@oregonstate.edu, ID 932194174), INSERT DAVID
# Course: OSU CS 362, Winter 2020
# Assignment: Final Project
# Assignment specification:
# Part A: https://oregonstate.instructure.com/courses/1750847/assignments/7761142
# Part B: https://oregonstate.instructure.com/courses/1750847/assignments/7761143
# Last modified: 10 March 2020
# Description:
# This program implements unit test test cases for Calculator class functions found in calculator.py.
# The calculator functions tested, the test strategy for each function, and the test pass/fail criteria
# are described in the Test Plan document created for Final Project Part A requirements linked above.


import unittest
import sys
import calculator


class TestCase(unittest.TestCase):

    # Invalid data test case 1 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is a string consisting of number characters.
    def test_multiply_invalidData_case1(self):
        # Initialize the test data.
        input1 = 77
        input2 = "12345"

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 2 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is a character form of a number.
    def test_multiply_invalidData_case2(self):
        # Initialize the test data.
        input1 = '9'
        input2 = 12

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 3 for multiply() function
    # Description:
    # Check that multiply() returns None when one input is a list containing two or more numbers and the
    # second input is a tuple containing two or more numbers.
    def test_multiply_invalidData_case3(self):
        # Initialize the test data.
        input1 = [1, 2, 54]
        input2 = (7, 8, 99)

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 4 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is a complex number.
    def test_multiply_invalidData_case4(self):
        # Initialize the test data.
        input1 = complex(7, 7)
        input2 = 999

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 5 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is a boolean.
    def test_multiply_invalidData_case5(self):
        # Initialize the test data.
        input1 = True
        input2 = 999

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 6 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is None.
    def test_multiply_invalidData_case6(self):
        # Initialize the test data.
        input1 = None
        input2 = 999

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 7 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is a valid type that has a numerical value
    # greater than sys.maxsize.
    def test_multiply_invalidData_case7(self):
        # Initialize the test data.
        input1 = sys.maxsize + 30
        input2 = -36

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 8 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is a valid type that has a numerical value
    # less than -sys.maxsize.
    def test_multiply_invalidData_case8(self):
        # Initialize the test data.
        input1 = 5
        input2 = -sys.maxsize - 10

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 9 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is a valid type that has a numerical value
    # greater than sys.maxsize that is a positive infinite float.
    def test_multiply_invalidData_case9(self):
        # Initialize the test data.
        input1 = float("inf")
        input2 = -36

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Invalid data test case 10 for multiply() function
    # Description:
    # Check that multiply() returns None when an input is a valid type that has a numerical value
    # less than -sys.maxsize that is a negative infinite float.
    def test_multiply_invalidData_case10(self):
        # Initialize the test data.
        input1 = 5
        input2 = -float("inf")

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(multiplyOutput)

    # Valid non-edge case data test case 1 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # that are positive integer values.
    def test_multiply_validNonEdgeCaseData_case1(self):
        # Initialize the test data.
        input1 = 2
        input2 = 30000
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 2 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # that are negative integer values.
    def test_multiply_validNonEdgeCaseData_case2(self):
        # Initialize the test data.
        input1 = -999
        input2 = -34
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 3 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is a positive integer and input2 is a negative integer.
    def test_multiply_validNonEdgeCaseData_case3(self):
        # Initialize the test data.
        input1 = 121212
        input2 = -797979
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 4 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is a positive integer and input2 is a positive fraction.
    def test_multiply_validNonEdgeCaseData_case4(self):
        # Initialize the test data.
        input1 = 11
        input2 = 1/3
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 5 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is a positive fraction and input2 is a negative fraction.
    def test_multiply_validNonEdgeCaseData_case5(self):
        # Initialize the test data.
        input1 = -9/37
        input2 = 12/13
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 6 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is a negative float and input2 is a positive fraction.
    def test_multiply_validNonEdgeCaseData_case6(self):
        # Initialize the test data.
        input1 = -99.99999
        input2 = 20/333
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 7 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is a negative float less than -1 and input2 is a negative float greater than -1.
    def test_multiply_validNonEdgeCaseData_case7(self):
        # Initialize the test data.
        input1 = -88.8879
        input2 = -0.4567456
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 1 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is equal to 0 and input2 is a negative number.
    def test_multiply_validEdgeCaseData_case1(self):
        # Initialize the test data.
        input1 = 0.00000
        input2 = -87

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(0, multiplyOutput)

    # Valid non-edge case data test case 2 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # that are zero.
    def test_multiply_validEdgeCaseData_case2(self):
        # Initialize the test data.
        input1 = 0.000
        input2 = 0

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(0, multiplyOutput)

    # Valid non-edge case data test case 3 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is equal to sys.maxsize and input2 is equal to sys.maxsize.
    def test_multiply_validEdgeCaseData_case3(self):
        # Initialize the test data.
        input1 = sys.maxsize
        input2 = sys.maxsize
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 4 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is equal to sys.maxsize and input2 is equal to -sys.maxsize.
    def test_multiply_validEdgeCaseData_case4(self):
        # Initialize the test data.
        input1 = sys.maxsize
        input2 = -sys.maxsize
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 5 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is equal to -sys.maxsize and input2 is equal to -sys.maxsize.
    def test_multiply_validEdgeCaseData_case5(self):
        # Initialize the test data.
        input1 = -sys.maxsize
        input2 = -sys.maxsize
        expectedProduct = input1 * input2

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedProduct, multiplyOutput)

    # Valid non-edge case data test case 6 for multiply() function
    # Description:
    # Check that multiply() returns the expected product when both inputs are valid numerical types
    # where input1 is equal to sys.maxsize and input2 is equal to 0.
    def test_multiply_validEdgeCaseData_case6(self):
        # Initialize the test data.
        input1 = sys.maxsize
        input2 = 0

        # Call the function under test.
        multiplyOutput = calculator.Calculator.multiply(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(0, multiplyOutput)
