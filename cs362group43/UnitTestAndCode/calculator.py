# Author: INSERT CHRIS, Ricardo Cousins (cousinsr@oregonstate.edu, ID 932194174), INSERT DAVID
# Course: OSU CS 362, Winter 2020
# Assignment: Final Project
# Assignment specification:
# Part A: https://oregonstate.instructure.com/courses/1750847/assignments/7761142
# Part B: https://oregonstate.instructure.com/courses/1750847/assignments/7761143
# Last modified: 10 March 2020
# Description:
# This program implements a Calculator class containing functions that perform the reduced set of calculator
# operations specified in the Final Project requirements linked above. The calculator functions are described
# in the Test Plan document created for Final Project Part A requirements linked above.
import math
import sys
# Calculator class
class Calculator:

    # This function takes two numerical inputs of type int or float, and returns the product of the inputs.
    # If either input provided is not of type int or float, the function returns None.
    # If either input provided is outside the range -sys.maxsize <= input <= sys.maxsize, the function returns None.
    # This function expects that two numerical inputs are provided.
    def multiply(input1, input2):
        return None

    # This function takes two numerical inputs of type int or float, and returns the quotient of input1 / input2.
    # If either input provided is not of type int or float, the function returns None.
    # If either input provided is outside the range -sys.maxsize <= input <= sys.maxsize, the function returns None.
    # If input2 equals 0, the function returns None.
    # This function expects that two numerical inputs are provided.
    def divide(input1, input2):
        return None

    # This function takes one numerical input of type int or float, and returns the square of the input.
    # If the input provided is not of type int or float, the function returns None.
    # If the input provided is outside the range -sys.maxsize <= input <= sys.maxsize, the function returns None.
    # This function expects that one numerical input is provided.
    def square(input1):
        return input1 * input1;

    # This function takes one numerical input of type int or float, and returns the absolute value of the input.
    # If the input provided is not of type int or float, the function returns None.
    # If the input provided is outside the range -sys.maxsize <= input <= sys.maxsize, the function returns None.
    # This function expects that one numerical input is provided.
    @staticmethod
    def absolute(input1):
        if type(input1) != int and type(input1) != float:
            return None
        if input1 > sys.maxsize:
            return None
        if input1 < -1 * sys.maxsize:
            return None
        if input1 >= 0:
            return input1
        else:
            inverse = input1 * (-2)
            total = input1 + inverse
            return total

    # This function takes one numerical input of type int or float, and returns the sine of the input in radians.
    # If the input provided is not of type int or float, the function returns None.
    # If the input provided is outside the range -sys.maxsize <= input <= sys.maxsize, the function returns None.
    # This function expects that one numerical input is provided.
    #https://www.quora.com/How-do-I-calculate-cos-sine-etc-without-a-calculator
    @staticmethod
    def sine(input1):
        if type(input1) != int and type(input1) != float:
            return None
        if input1 > sys.maxsize:
            return None
        if input1 < -1 * sys.maxsize:
            return None
        prepInput = input1
        if Calculator.absolute(prepInput) == (2 * math.pi):
            return 0
        if Calculator.absolute(prepInput) > (2 * math.pi):
            divisor = math.modf(prepInput / (2 * math.pi))
            prepInput = (2 * math.pi) * divisor[0]
        if prepInput < 0:
            prepInput = prepInput + (2 * math.pi)
        temp = (prepInput*prepInput*prepInput) / 6
        total = prepInput - temp
        temp = (prepInput*prepInput*prepInput*prepInput*prepInput) / 120
        total = total + temp
        temp = (prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput) / 5040
        total = total - temp
        temp = (prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput) / 362880
        total = total + temp
        temp = (prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput*prepInput) / 39916800
        total = total - temp
        temp = (prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput) / 6227020800
        total = total + temp
        temp = (prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput) / 1307674368000
        total = total - temp
        return total


    # This function takes one numerical input of type int or float, and returns the cosine of the input in radians.
    # If the input provided is not of type int or float, the function returns None.
    # If the input provided is outside the range -sys.maxsize <= input <= sys.maxsize, the function returns None.
    # This function expects that one numerical input is provided.
    def cosine(input1):
        if type(input1) != int and type(input1) != float:
            return None
        if input1 > sys.maxsize:
            return None
        if input1 < -1 * sys.maxsize:
            return None
        prepInput = input1
        if Calculator.absolute(prepInput) == (2 * math.pi):
            return 1
        if Calculator.absolute(prepInput) > (2 * math.pi):
            divisor = math.modf(prepInput / (2 * math.pi))
            prepInput = (2 * math.pi) * divisor[0]
        if prepInput < 0:
            prepInput = prepInput + (2 * math.pi)
        temp = (prepInput * prepInput) / 2
        total = 1 - temp
        temp = (prepInput * prepInput * prepInput * prepInput) / 24
        total = total + temp
        temp = (prepInput * prepInput * prepInput * prepInput * prepInput * prepInput) / 720
        total = total - temp
        temp = (prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput) / 40320
        total = total + temp
        temp = (prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput) / 3628800
        total = total - temp
        temp = (prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput) / 479001600
        total = total + temp
        temp = (prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput * prepInput) / 87178291200
        total = total - temp
        return total

    # This function takes one numerical input of type int or float, and returns the square root of the input.
    # If the input provided is not of type int or float, the function returns None.
    # If the input provided is outside the range 0 <= input <= sys.maxsize, the function returns None.
    # This function expects that one numerical input is provided.
    @staticmethod
    def SQRT(input1):
        if input1 is None or isinstance(input1, str) or isinstance(input1, list) or\
                isinstance(input1, tuple) or isinstance(input1, complex) or isinstance(input1, bool) or input1 < 0 :
            return None
        elif input1 > sys.maxsize:
            return None
        elif input1 == math.inf or input1 == -1 * math.inf:
            return None
        else:
            return input1**.5
    # This function takes one numerical input of type int or float (with decimal = 0 eg 1.0), and returns the factorial of the input.
    # If the input provided is not of type int or float (with decimal = 0 eg 1.0), the function returns None.
    # If the input provided is outside the range 0 <= input <= 100, the function returns None.
    # This function expects that one numerical input is provided.

    @staticmethod
    def factorial(input1):
        if input1 is None or isinstance(input1, str) or isinstance(input1, list) or\
                isinstance(input1, tuple) or isinstance(input1, complex) or isinstance(input1, bool) or input1 < 0:
            return None
        elif input1 > 100:
            return None
        elif isinstance(input1, float) and not input1.is_integer():
            return None
        else:
            result = 1
            while input1 != 0:
                result = input1 * result
                input1 = input1 - 1
        return result
        
    # This function takes one numerical input of type int or float, and returns the inverse (1/x) of the input.
    # If the input provided is not of type int or float, the function returns None.
    # If the input provided is outside the range -sys.maxsize <= input <= sys.maxsize, or if the input is zero, the function returns None.
    # This function expects that one numerical input is provided.
    @staticmethod
    def inverse(input1):
        if input1 == 0 or input1 == 0.0 or input1 is None or isinstance(input1, str) or isinstance(input1, list) or\
                isinstance(input1, tuple) or isinstance(input1, complex) or isinstance(input1, bool):
            return None
        elif input1 > sys.maxsize:
            return None
        elif input1 < -1 * sys.maxsize:
            return None
        elif input1 == math.inf or input1 == -1 * math.inf:
            return None
        else:
            return 1 / input1

        

