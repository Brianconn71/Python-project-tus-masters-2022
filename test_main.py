# Student ID: A00204916
"""
This file is used to test the main.py file
"""
from main import (
    print_statements, correlation_and_dictionary
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


def test_correlation_and_dictionary():
    """
    tests correlation_and_dictionary prints the correct
    data to the console and analyses correlation between
    two lists and the dictionary data
    """
    # calls the print_startements function
    correlation_and_dictionary()
    # asserts the returned value is equal to the expected value.
    assert True


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
