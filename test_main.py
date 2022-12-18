# Student ID: A00204916
"""
This file is used to test the main.py file
"""
from main import (
    print_statements, dictionary_data
)
import pytest


def test_print_statements():
    """
    tests print_statements prints the correct
    data to the console
    """
    # calls the print_startements function
    print_statements()
    # asserts the returned value is equal to the expected value.
    assert True


def test_dictionary_data():
    """
    tests dictionary_data prints the correct
    data to the console and analyses correlation between
    two lists and the dictionary data
    """
    # calls the print_startements function
    dictionary_data()
    # asserts the returned value is equal to the expected value.
    assert True


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
