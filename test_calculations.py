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


def test_get_number_of_games_in_season():
    output = get_number_of_games_in_season()
    assert output == 380


def test_get_total_fouls_per_game_in_season():
    output = get_total_fouls_per_game_in_season()
    assert len(output) == 380
    assert type(output) == list


def test_get_average_fouls_per_game():
    output = get_average_fouls_per_game(380)
    assert output == pytest.approx(20.21)


def test_get_median_fouls_per_game():
    output = get_median_fouls_per_game([1, 2, 3, 4, 5])
    assert output == 3


def test_get_mode_fouls_per_game():
    output = get_mode_fouls_per_game([1, 2, 2, 4, 5])
    assert output == 2


def test_get_maximum_fouls_in_a_game():
    output = get_maximum_fouls_in_a_game([2, 3, 1, 7, 5])
    assert output == pytest.approx(7)


def test_get_minimum_fouls_in_a_game():
    output = get_minimum_fouls_in_a_game([2, 3, 1, 7, 5])
    assert output == pytest.approx(1)


def test_get_range_of_fouls():
    output = get_range_of_fouls(5, 3)
    assert output == "3, 5"


def test_get_interquartile_range_of_fouls():
    output = get_interquartile_range_of_fouls([2.2, 3.5, 1.5, 7.3, 5.0])
    assert output == pytest.approx(4.3)


def test_get_standard_deviation_of_fouls():
    output = get_standard_deviation_of_fouls([19, 20, 20, 40, 50])
    assert output == pytest.approx(14, 0.1)


def test_get_pearson_mode_skewness_of_fouls():
    output = get_pearson_mode_skewness_of_fouls([19, 20, 20, 40, 50])
    assert output == pytest.approx(0.6, 0.2)


def test_get_alternative_pearson_mode_skewness_of_fouls():
    output = (
        get_alternative_pearson_mode_skewness_of_fouls([19, 20, 20, 40, 50]))
    assert output == pytest.approx(2, 0.1)


def test_get_covariance_between_datasets():
    output = (
        get_covariance_between_datasets([23, 45, 32, 12, 34],
                                        [19, 20, 20, 40, 50]))
    assert output == pytest.approx(-38, 0.1)


def test_get_correlation_of_fouls():
    output = (
        get_correlation_of_fouls([23, 45, 32, 12, 34], [19, 20, 20, 40, 50]))
    assert output == pytest.approx(-0.25, 0.1)


if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data
    # from csv and split into lists
    read_data_and_create_lists()
    pytest.main(["test_calculations.py", "-vv"])
