# Student ID: A00204916
"""
This file is used to test the calculations on the categorical data
"""
from dictionary_calculations import (
    get_dict_of_refs_and_occurances_in_data,
    get_total_refs_data, distinct_sub_categories,
    dict_from_average_fouls_per_game,
    ref_with_most_fouls_given, ref_with_least_fouls_given,
    ref_with_highest_average_of_fouls_given_per_game,
    ref_with_lowest_average_of_fouls_given_per_game
)
from calculations import read_data_and_create_lists
import pytest


def test_get_dict_of_refs_and_occurances_in_data():
    """
    tests that get_dict_of_refs_and_occurances_in_data function
    will turn a list into a dictionary.
    """
    # calls get_dict_of_refs_and_occurances_in_data with list of strings
    output = get_dict_of_refs_and_occurances_in_data(
        ["B connolly", "A man", "Walter weatherman"])
    # asserts length of dictionary keys will be three
    assert len(output.keys()) == 3
    # asserts type returned is a dictionary
    assert type(output) == dict


def test_get_total_refs_data():
    """
    tests that get_total_refs_data function
    will turn two lists into a dictionary with keys and relevant values.
    """
    # calls get_total_refs_data with two lists
    output = get_total_refs_data(
        ["B connolly", "A man", "Walter weatherman"], [3, 4, 5])
    # asserts output is type dictionary
    assert type(output) == dict
    # asserts keys have correct values
    assert output["B connolly"] == 3


def test_distinct_sub_categories():
    """
    tests that distinct_sub_categories function will return
    an integer value represnting number of keys in the dictionary
    """
    # calls distinct_sub_categories with a dictinary
    output = distinct_sub_categories({"B connolly": 3, "A man": 4})
    # asserts the distinct value is 2
    assert output == 2


def test_dict_from_average_fouls_per_game():
    """
    tests that dict_from_average_fouls_per_game function will return
    an dictionary with average value as a float and type dictionary
    """
    # calls dict_from_average_fouls_per_game with two dictionaries
    output = dict_from_average_fouls_per_game(
        {"B connolly": 3, "A man": 4}, {"B connolly": 6, "A man": 7})
    # asserts keys have the correct values
    assert output["B connolly"] == pytest.approx(0.5)
    # asserts output type is a dictionary
    assert type(output) == dict


def test_ref_with_most_fouls_given():
    """
    tests that ref_with_most_fouls_given function will return
    a string value.
    """
    # calls ref_with_most_fouls_given with a dictionary
    output = ref_with_most_fouls_given({"B connolly": 13, "A man": 4})
    # asserts the output has the correct values from dictionaries passed above
    assert output == (
        "The referee who gave the most fouls in the 2021/22 season was: "
        "B connolly with a total fouls given of 13")
    # asserts return is of type string
    assert type(output) == str


def test_ref_with_least_fouls_given():
    """
    tests that ref_with_least_fouls_given function will return
    a string value.
    """
    # calls ref_with_least_fouls_given with a dictionary
    output = ref_with_least_fouls_given({"B connolly": 13, "A man": 4})
    # asserts the output has the correct values from dictionaries passed above
    assert output == ("The referee who gave the least fouls in the 2021/22"
                      " season was: A man with a total fouls given of 4")
    # asserts return is of type string
    assert type(output) == str


def test_ref_with_highest_average_of_fouls_given_per_game():
    """
    tests that ref_with_highest_average_of_fouls_given_per_game
    function will return a string value.
    """
    # calls ref_with_highest_average_of_fouls_given_per_game with a dictionary
    output = ref_with_highest_average_of_fouls_given_per_game(
        {"B connolly": 13.45, "A man": 4.3})
    # asserts the output has the correct values from dictionaries passed above
    assert output == ("The referee who had the highest average of fouls"
                      " given per game in the 2021/22 season was: B connolly"
                      " with an average fouls per game of 13.45")
    # asserts return is of type string
    assert type(output) == str


def test_ref_with_lowest_average_of_fouls_given_per_game():
    """
    tests that ref_with_lowest_average_of_fouls_given_per_game
    function will return a string value.
    """
    # calls ref_with_lowest_average_of_fouls_given_per_game with a dictionary
    output = ref_with_lowest_average_of_fouls_given_per_game(
        {"B connolly": 13.45, "A man": 4.3})
    # asserts the output has the correct values from dictionaries passed above
    assert output == (
        "The referee who had the lowest average of fouls given"
        " per game in the 2021/22 season was: A man with an average"
        " fouls per game of 4.3 ")
    # asserts return is of type string
    assert type(output) == str


if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data
    # from csv and split into lists
    read_data_and_create_lists()
    pytest.main([__file__, "-vv"])
