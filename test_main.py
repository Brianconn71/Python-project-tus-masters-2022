from main import *
import pytest

def test_print_statements():
    """
    tests print_statements prins the correct
    data to the console
    """
    # calls the read_data_and_create_lists function
    output = print_statements()
    # asserts the returned value is equal to the expected value.
    assert output == 380