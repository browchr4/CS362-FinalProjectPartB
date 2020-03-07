# Author: INSERT CHRIS, Ricardo Cousins (cousinsr@oregonstate.edu, ID 932194174), David Passaro (passarod@oregonstate.edu)
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
    # where input1 is a negative fraction and input2 is a positive fraction.
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

    # Valid edge case data test case 1 for multiply() function
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

    # Valid edge case data test case 2 for multiply() function
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

    # Valid edge case data test case 3 for multiply() function
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

    # Valid edge case data test case 4 for multiply() function
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

    # Valid edge case data test case 5 for multiply() function
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

    # Valid edge case data test case 6 for multiply() function
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

    # Invalid data test case 1 for divide() function
    # Description:
    # Check that divide() returns None when an input is a string consisting of number characters.
    def test_divide_invalidData_case1(self):
        # Initialize the test data.
        input1 = 77
        input2 = "12345"

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 2 for divide() function
    # Description:
    # Check that divide() returns None when an input is a character form of a number.
    def test_divide_invalidData_case2(self):
        # Initialize the test data.
        input1 = '9'
        input2 = 12

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 3 for divide() function
    # Description:
    # Check that divide() returns None when one input is a list containing two or more numbers and the
    # second input is a tuple containing two or more numbers.
    def test_divide_invalidData_case3(self):
        # Initialize the test data.
        input1 = [1, 2, 54]
        input2 = (7, 8, 99)

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 4 for divide() function
    # Description:
    # Check that divide() returns None when an input is a complex number.
    def test_divide_invalidData_case4(self):
        # Initialize the test data.
        input1 = complex(7, 7)
        input2 = 999

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 5 for divide() function
    # Description:
    # Check that divide() returns None when an input is a boolean.
    def test_divide_invalidData_case5(self):
        # Initialize the test data.
        input1 = True
        input2 = 999

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 6 for divide() function
    # Description:
    # Check that divide() returns None when an input is None.
    def test_divide_invalidData_case6(self):
        # Initialize the test data.
        input1 = None
        input2 = 999

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 7 for divide() function
    # Description:
    # Check that divide() returns None when an input is a valid type that has a numerical value
    # greater than sys.maxsize.
    def test_divide_invalidData_case7(self):
        # Initialize the test data.
        input1 = sys.maxsize + 30
        input2 = -36

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 8 for divide() function
    # Description:
    # Check that divide() returns None when an input is a valid type that has a numerical value
    # less than -sys.maxsize.
    def test_divide_invalidData_case8(self):
        # Initialize the test data.
        input1 = 5
        input2 = -sys.maxsize - 10

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 9 for divide() function
    # Description:
    # Check that divide() returns None when an input is a valid type that has a numerical value
    # greater than sys.maxsize that is a positive infinite float.
    def test_divide_invalidData_case9(self):
        # Initialize the test data.
        input1 = float("inf")
        input2 = -36

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 10 for divide() function
    # Description:
    # Check that divide() returns None when an input is a valid type that has a numerical value
    # less than -sys.maxsize that is a negative infinite float.
    def test_divide_invalidData_case10(self):
        # Initialize the test data.
        input1 = 5
        input2 = -float("inf")

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Invalid data test case 11 for divide() function
    # Description:
    # Check that divide() returns None when input2 is a valid type that has a numerical value of zero.
    def test_divide_invalidData_case11(self):
        # Initialize the test data.
        input1 = 5
        input2 = 0.000

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertIsNone(divideOutput)

    # Valid non-edge case data test case 1 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # that are positive integer values.
    def test_divide_validNonEdgeCaseData_case1(self):
        # Initialize the test data.
        input1 = 2
        input2 = 30000
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid non-edge case data test case 2 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # that are negative integer values.
    def test_divide_validNonEdgeCaseData_case2(self):
        # Initialize the test data.
        input1 = -999
        input2 = -34
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid non-edge case data test case 3 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is a positive integer and input2 is a negative integer.
    def test_divide_validNonEdgeCaseData_case3(self):
        # Initialize the test data.
        input1 = 121212
        input2 = -797979
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid non-edge case data test case 4 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is a positive integer and input2 is a positive fraction.
    def test_divide_validNonEdgeCaseData_case4(self):
        # Initialize the test data.
        input1 = 11
        input2 = 1/3
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid non-edge case data test case 5 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is a negative fraction and input2 is a positive fraction.
    def test_divide_validNonEdgeCaseData_case5(self):
        # Initialize the test data.
        input1 = -9/37
        input2 = 12/13
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid non-edge case data test case 6 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is a negative float and input2 is a positive fraction.
    def test_divide_validNonEdgeCaseData_case6(self):
        # Initialize the test data.
        input1 = -99.99999
        input2 = 20/333
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid non-edge case data test case 7 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is a negative float less than -1 and input2 is a negative float greater than -1.
    def test_divide_validNonEdgeCaseData_case7(self):
        # Initialize the test data.
        input1 = -88.8879
        input2 = -0.4567456
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid edge case data test case 1 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is equal to 0 and input2 is a negative number.
    def test_divide_validEdgeCaseData_case1(self):
        # Initialize the test data.
        input1 = 0.00000
        input2 = -87

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(0, divideOutput)

    # Valid edge case data test case 2 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is equal to sys.maxsize and input2 is equal to sys.maxsize.
    def test_divide_validEdgeCaseData_case2(self):
        # Initialize the test data.
        input1 = sys.maxsize
        input2 = sys.maxsize
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid edge case data test case 3 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is equal to sys.maxsize and input2 is equal to -sys.maxsize.
    def test_divide_validEdgeCaseData_case3(self):
        # Initialize the test data.
        input1 = sys.maxsize
        input2 = -sys.maxsize
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid edge case data test case 4 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is equal to -sys.maxsize and input2 is equal to -sys.maxsize.
    def test_divide_validEdgeCaseData_case4(self):
        # Initialize the test data.
        input1 = -sys.maxsize
        input2 = -sys.maxsize
        expectedQuotient = input1 / input2

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(expectedQuotient, divideOutput)

    # Valid edge case data test case 5 for divide() function
    # Description:
    # Check that divide() returns the expected quotient when both inputs are valid numerical types
    # where input1 is equal to 0 and input2 is equal to sys.maxsize.
    def test_divide_validEdgeCaseData_case5(self):
        # Initialize the test data.
        input1 = 0
        input2 = sys.maxsize

        # Call the function under test.
        divideOutput = calculator.Calculator.divide(input1, input2)

        # Assert expectations after the function call.
        self.assertEqual(0, divideOutput)

    # Invalid data test case 1 for square() function
    # Description:
    # Check that square() returns None when an input is a string consisting of number characters.
    def test_square_invalidData_case1(self):
        # Initialize the test data.
        input1 = "12345"

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 2 for square() function
    # Description:
    # Check that square() returns None when an input is a character form of a number.
    def test_square_invalidData_case2(self):
        # Initialize the test data.
        input1 = '9'

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 3 for square() function
    # Description:
    # Check that square() returns None when the input is a list containing two or more numbers.
    def test_square_invalidData_case3(self):
        # Initialize the test data.
        input1 = [1, 2, 54]

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 4 for square() function
    # Description:
    # Check that square() returns None when an input is a complex number.
    def test_square_invalidData_case4(self):
        # Initialize the test data.
        input1 = complex(7, 7)

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 5 for square() function
    # Description:
    # Check that square() returns None when an input is a boolean.
    def test_square_invalidData_case5(self):
        # Initialize the test data.
        input1 = True

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 6 for square() function
    # Description:
    # Check that square() returns None when an input is None.
    def test_square_invalidData_case6(self):
        # Initialize the test data.
        input1 = None

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 7 for square() function
    # Description:
    # Check that square() returns None when an input is a valid type that has a numerical value
    # greater than sys.maxsize.
    def test_square_invalidData_case7(self):
        # Initialize the test data.
        input1 = sys.maxsize + 30

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 8 for square() function
    # Description:
    # Check that square() returns None when an input is a valid type that has a numerical value
    # less than -sys.maxsize.
    def test_square_invalidData_case8(self):
        # Initialize the test data.
        input1 = -sys.maxsize - 10

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 9 for square() function
    # Description:
    # Check that square() returns None when an input is a valid type that has a numerical value
    # greater than sys.maxsize that is a positive infinite float.
    def test_square_invalidData_case9(self):
        # Initialize the test data.
        input1 = float("inf")

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Invalid data test case 10 for square() function
    # Description:
    # Check that square() returns None when an input is a valid type that has a numerical value
    # less than -sys.maxsize that is a negative infinite float.
    def test_square_invalidData_case10(self):
        # Initialize the test data.
        input1 = -float("inf")

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertIsNone(squareOutput)

    # Valid non-edge case data test case 1 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is a positive integer value.
    def test_square_validNonEdgeCaseData_case1(self):
        # Initialize the test data.
        input1 = 30000
        expectedSquare = input1 * input1

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(expectedSquare, squareOutput)

    # Valid non-edge case data test case 2 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is a negative integer value.
    def test_square_validNonEdgeCaseData_case2(self):
        # Initialize the test data.
        input1 = -999
        expectedSquare = input1 * input1

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(expectedSquare, squareOutput)

    # Valid non-edge case data test case 3 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is a positive fraction.
    def test_square_validNonEdgeCaseData_case3(self):
        # Initialize the test data.
        input1 = 1/3
        expectedSquare = input1 * input1

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(expectedSquare, squareOutput)

    # Valid non-edge case data test case 4 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is a negative fraction.
    def test_square_validNonEdgeCaseData_case4(self):
        # Initialize the test data.
        input1 = -9/37
        expectedSquare = input1 * input1

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(expectedSquare, squareOutput)

    # Valid non-edge case data test case 5 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is a negative float less than -1.
    def test_square_validNonEdgeCaseData_case5(self):
        # Initialize the test data.
        input1 = -99.99999
        expectedSquare = input1 * input1

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(expectedSquare, squareOutput)

    # Valid non-edge case data test case 6 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is a negative float greater than -1.
    def test_square_validNonEdgeCaseData_case6(self):
        # Initialize the test data.
        input1 = -0.4567456
        expectedSquare = input1 * input1

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(expectedSquare, squareOutput)

    # Valid edge case data test case 1 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is equal to 0.
    def test_square_validEdgeCaseData_case1(self):
        # Initialize the test data.
        input1 = 0.00000

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(0, squareOutput)

    # Valid edge case data test case 2 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is equal to sys.maxsize.
    def test_square_validEdgeCaseData_case2(self):
        # Initialize the test data.
        input1 = sys.maxsize
        expectedSquare = input1 * input1

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(expectedSquare, squareOutput)

    # Valid edge case data test case 3 for square() function
    # Description:
    # Check that square() returns the expected square when the input is a valid numerical type
    # that is equal to -sys.maxsize.
    def test_square_validEdgeCaseData_case3(self):
        # Initialize the test data.
        input1 = -sys.maxsize
        expectedSquare = input1 * input1

        # Call the function under test.
        squareOutput = calculator.Calculator.square(input1)

        # Assert expectations after the function call.
        self.assertEqual(expectedSquare, squareOutput)
'''




















#David section begin

'''
'''Invalid Data Test Cases
Test Case 1
Check that SQRT() returns None when an input is a string consisting of number characters.'''

    def test_SQRT_invalidData_case1(self):
        # Initialize the test data.
        input1 = '09'

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case2(self):
        # Initialize the test data.
        input1 = '9'

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case3(self):
        # Initialize the test data.
        input1 = [1, 2, 54]

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case4(self):
        # Initialize the test data.
        input1 = complex(7, 7)

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case5(self):
        # Initialize the test data.
        input1 = True

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case6(self):
        # Initialize the test data.
        input1 = None

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case7(self):
        # Initialize the test data.
        input1 = sys.maxsize + 5

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case8(self):
        # Initialize the test data.
        input1 = -1

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case9(self):
        # Initialize the test data.
        input1 =  float(“inf”)

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_SQRT_invalidData_case10(self):
        # Initialize the test data.
        input1 =  -sys.maxsize

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    #Valid Non-Edge Case Data Test Cases
    def test_SQRT_validNonEdgeCaseData_case1(self):
        # Initialize the test data.
        input1 = 4

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertEqual(SQRTOutput, math.sqrt(4))

    def test_SQRT_validNonEdgeCaseData_case2(self):
        # Initialize the test data.
        input1 = 1/3

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertEqual(SQRTOutput, math.sqrt(1/3))

    def test_SQRT_validNonEdgeCaseData_case3(self):
        # Initialize the test data.
        input1 = 3.333

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertEqual(SQRTOutput, math.sqrt(3.333))

    #Valid Edge Case Data Test Cases
    def test_SQRT_validEdgeCaseData_case1(self):
        # Initialize the test data.
        input1 = 0.00000

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertEqual(SQRTOutput, math.sqrt(0.00000))
    
    def test_SQRT_validEdgeCaseData_case2(self):
        # Initialize the test data.
        input1 = sys.maxsize

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertEqual(SQRTOutput, math.sqrt(sys.maxsize))
'''


Inverse



'''
#Invalid Data Test Cases
    def test_inverse_invalidData_case1(self):
        # Initialize the test data.
        input1 = '99'

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case2(self):
        # Initialize the test data.
        input1 = '9'

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case3(self):
        # Initialize the test data.
        input1 =  [1, 2, 54]

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case4(self):
        # Initialize the test data.
        input1 = complex(7, 7)

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)


    def test_inverse_invalidData_case5(self):
        # Initialize the test data.
        input1 = True

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case6(self):
        # Initialize the test data.
        input1 = None

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case7(self):
        # Initialize the test data.
        input1 = sys.maxsize + 30

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case9(self):
        # Initialize the test data.
        input1 = -sys.maxsize - 3

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case10(self):
        # Initialize the test data.
        input1 =  float(“inf”)

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case10(self):
        # Initialize the test data.
        input1 =  -float(“inf”)

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case10(self):
        # Initialize the test data.
        input1 =  0

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)

    def test_inverse_invalidData_case10(self):
        # Initialize the test data.
        input1 =  (1,2 )

        # Call the function under test.
        SQRTOutput = calculator.Calculator.SQRT(input1)

        # Assert expectations after the function call.
        self.assertIsNone(SQRTOutput)



 