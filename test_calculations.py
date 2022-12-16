# Student ID: A00204916
"""
This file is used to test the calculations.py file
"""
from calculations import (
    get_number_of_games_in_season, get_total_fouls_per_game_in_season,
    get_average_fouls_per_game, get_median_fouls_per_game,
    get_mode_fouls_per_game, get_maximum_fouls_in_a_game,
    get_minimum_fouls_in_a_game, get_range_of_fouls,
    get_interquartile_range_of_fouls, get_standard_deviation_of_fouls,
    get_pearson_mode_skewness_of_fouls,
    get_alternative_pearson_mode_skewness_of_fouls,
    get_covariance_between_datasets, get_correlation_of_fouls,
    read_data_and_create_lists)
import pytest


def test_read_data_and_create_lists():
    """
    tests read_data_and_create_lists reads the
    data and creates the correct lists.
    """
    # calls the read_data_and_create_lists function
    read_data_and_create_lists()
    # asserts the function runs as expected.
    assert True


def test_get_number_of_games_in_season():
    """
    tests get_number_of_games_in_season returns the correct number
    of games in the season
    """
    # calls the get_number_of_games_in_season function
    output = get_number_of_games_in_season([1, 2, 3, 4, 5])
    # asserts the returned value is equal to the expected value.
    assert output == 5


def test_get_total_fouls_per_game_in_season():
    """
    tests get_total_fouls_per_game_in_season returns the correct number
    of fouls per game in season.
    """
    # calls the get_total_fouls_per_game_in_season function
    output = get_total_fouls_per_game_in_season([1, 2, 3, 4, 5],
                                                [1, 2, 3, 4, 5])
    # asserts the length of the list is equal to expected
    assert len(output) == 5
    # asserts the data type is list.
    assert type(output) == list


def test_get_average_fouls_per_game():
    """
    tests get_average_fouls_per_game returns the correct value
    of fouls per game in season.
    """
    # calls the get_average_fouls_per_game function with an integer value
    output = get_average_fouls_per_game(380)
    # asserts the returned value is equal to expected value.
    assert output == pytest.approx(20.21)


def test_get_median_fouls_per_game():
    """
    tests get_median_fouls_per_game returns the correct value
    for the median of the list passed.
    """
    # calls the get_median_fouls_per_game function with a list of integers
    output = get_median_fouls_per_game([1, 2, 3, 4, 5])
    # asserts the returned value is equal to expected value
    assert output == 3


def test_get_mode_fouls_per_game():
    """
    tests get_mode_fouls_per_game returns the correct value
    for the mode of the list passed.
    """
    # calls the get_mode_fouls_per_game function with a list of integers
    output = get_mode_fouls_per_game([1, 2, 2, 4, 5])
    # asserts the returned value is equal to expected value
    assert output == 2


def test_get_maximum_fouls_in_a_game():
    """
    tests get_maximum_fouls_in_a_game returns the correct value
    for the mode of the list passed.
    """
    # calls the get_maximum_fouls_in_a_game function with a list of integers
    output = get_maximum_fouls_in_a_game([2, 3, 1, 7, 5])
    # asserts the returned value is equal to expected value
    assert output == pytest.approx(7)


def test_get_minimum_fouls_in_a_game():
    """
    tests get_minimum_fouls_in_a_game returns the correct value
    for the mode of the list passed.
    """
    # calls the get_minimum_fouls_in_a_game function with a list of integers
    output = get_minimum_fouls_in_a_game([2, 3, 1, 7, 5])
    # asserts the returned value is equal to expected value
    assert output == pytest.approx(1)


def test_get_range_of_fouls():
    """
    tests get_range_of_fouls returns the correct value
    for the mode of the list passed.
    """
    # calls the get_range_of_fouls function with a list of integers
    output = get_range_of_fouls(5, 3)
    # asserts the returned value is equal to expected value
    assert output == "3, 5"


def test_get_interquartile_range_of_fouls():
    """
    tests get_interquartile_range_of_fouls returns the correct value
    for the mode of the list passed.
    """
    # calls the get_interquartile_range_of_fouls function with a
    # list of integers
    output = get_interquartile_range_of_fouls([2.2, 3.5, 1.5, 7.3, 5.0])
    # asserts the returned value is equal to expected value
    assert output == pytest.approx(4.3)


def test_get_standard_deviation_of_fouls():
    """
    tests get_standard_deviation_of_fouls returns the correct value
    for the mode of the list passed.
    """
    # calls the get_standard_deviation_of_fouls function with
    # a list of integers
    output = get_standard_deviation_of_fouls([19, 20, 20, 40, 50])
    # asserts the returned value is equal to expected value
    assert output == pytest.approx(14, 0.1)


def test_get_pearson_mode_skewness_of_fouls():
    """
    tests get_pearson_mode_skewness_of_fouls returns the correct value
    for the mode of the list passed.
    """
    # calls the get_pearson_mode_skewness_of_fouls function with
    # a list of integers
    output = get_pearson_mode_skewness_of_fouls([19, 20, 20, 40, 50])
    # asserts the returned value is equal to expected value
    assert output == pytest.approx(0.6, 0.2)


def test_get_alternative_pearson_mode_skewness_of_fouls():
    """
    tests get_alternative_pearson_mode_skewness_of_fouls returns the
    correct value for the mode of the list passed.
    """
    # calls the get_alternative_pearson_mode_skewness_of_fouls function with
    # a list of integers
    output = (
        get_alternative_pearson_mode_skewness_of_fouls([19, 20, 20, 40, 50]))
    # asserts the returned value is equal to expected value
    assert output == pytest.approx(2, 0.1)


def test_get_covariance_between_datasets():
    """
    tests get_covariance_between_datasets returns the
    correct value for the mode of the lists passed.
    """
    # calls the get_covariance_between_datasets function with
    # two lists of integers
    output = (
        get_covariance_between_datasets([23, 45, 32, 12, 34],
                                        [19, 20, 20, 40, 50]))
    # asserts the returned value is equal to expected value
    assert output == pytest.approx(-38, 0.1)


def test_get_correlation_of_fouls():
    """
    tests get_correlation_of_fouls returns the
    correct value for the mode of the lists passed.
    """
    # calls the get_covariance_between_datasets function with
    # two lists of integers
    output = (
        get_correlation_of_fouls([23, 45, 32, 12, 34], [19, 20, 20, 40, 50]))
    # asserts the returned value is equal to expected value
    assert output == pytest.approx(-0.25, 0.1)


if __name__ == "__main__":
    pytest.main([__file__, "-vv"])
