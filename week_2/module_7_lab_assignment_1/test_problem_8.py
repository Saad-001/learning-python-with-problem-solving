"""
8. Suppose you have a program that converts a string into Upper, Capitalized and Lower style using three different functions. Now create a test script for testing the three functionality of that program. Run using PyTest.

Write a function make_upper() to make the string in uppercase
Write a function make_capital() to make the string capitalized
Write a function make_lower() to make the string lowercase

Write a function named test_script() and write your code inside this function.

"""

import pytest

input_str = "PythOn"

def make_upper(text) :
    if not isinstance(text, str):
        raise TypeError('Please provide a string argument')
    text = text.upper()
    return text

def make_lower(text) :
    if not isinstance(text, str):
        raise TypeError('Please provide a string argument')
    text = text.lower()
    return text

def make_capital(text) :
    if not isinstance(text, str):
        raise TypeError('Please provide a string argument')
    text = text.capitalize()
    return text

def test_script() :
    assert make_upper(input_str) == input_str.upper()
    assert make_lower(input_str) == input_str.lower()
    assert make_capital(input_str) == input_str.capitalize()

test_script()
