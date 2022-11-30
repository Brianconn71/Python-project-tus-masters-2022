from calculations import *
import pytest

def test_read_data_and_create_lists():
    assert 1 ==1


def test_get_number_of_games_in_season():
    pass

def test_get_average_fouls_per_game():
    assert get_average_fouls_per_game(380) == 78


if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data from csv and split into lists
    read_data_and_create_lists()
    # uses the length of the home_fouls list (always has at least one value) to calculate total games
    total_games = len(home_fouls)
    # gets the average fouls per game in season from get_average_fouls_per_game function in calculations.py
    average_fouls = get_average_fouls_per_game(total_games)
    test_get_average_fouls_per_game(total_games)