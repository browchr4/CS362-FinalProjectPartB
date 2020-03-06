# Author: INSERT CHRIS, Ricardo Cousins (cousinsr@oregonstate.edu), INSERT DAVID
# Course: OSU CS 362, Winter 2020
# Assignment: Final Project
# Assignment specification:
# https://oregonstate.instructure.com/courses/1750847/assignments/7761142
# Last modified: 10 March 2020
# Description:
# This program implements unit test test cases for Calculator class functions found in calculator.py.


import unittest
import calculator


class TestCase(unittest.TestCase):

    # Test case 1 for circleArea() function
    # Description:
    # Check that circleArea() returns expected output when input radius equals zero.
    def test_multiplication_case1(self):
        # Initialize the test data.
        inputRadius = 0

        # Call the function under test.
        outputArea = task.circleArea(inputRadius)

        # Assert expectations after the function call.
        self.assertEqual(0, outputArea)

    # Test case 2 for circleArea() function
    # Description:
    # Check that circleArea() returns expected output when input radius is less than zero.
    def test_multiplication_case2(self):
        # Initialize the test data.
        inputRadius = -7

        # Call the function under test.
        outputArea = task.circleArea(inputRadius)

        # Assert expectations after the function call.
        self.assertIsNone(outputArea)
