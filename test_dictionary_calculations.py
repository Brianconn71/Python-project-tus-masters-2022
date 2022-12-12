from dictionary_calculations import *
from calculations import *
import pytest

def test_get_dict_of_refs_and_occurances_in_data():
    output = get_dict_of_refs_and_occurances_in_data(["B connolly", "A man", "Walter weatherman"])
    assert len(output.keys()) == 3
    assert type(output) == dict

def test_get_total_refs_data():
    output = get_total_refs_data(["B connolly", "A man", "Walter weatherman"], [3, 4, 5])
    assert type(output) == dict
    assert output["B connolly"] == 3

def test_distinct_sub_categories():
    output = distinct_sub_categories({"B connolly": 3, "A man": 4})
    assert output == 2

def test_dict_from_average_fouls_per_game():
    output = dict_from_average_fouls_per_game({"B connolly": 3, "A man": 4}, {"B connolly": 6, "A man": 7})
    assert output["B connolly"] == pytest.approx(0.5)

def test_ref_with_most_fouls_given():
    output = ref_with_most_fouls_given({"B connolly": 13, "A man": 4})
    assert output == "The referee who gave the most fouls in the 2021/22 season was: B connolly with a total fouls given of 13"
    assert type(output) == str

def test_ref_with_least_fouls_given():
    output = ref_with_least_fouls_given({"B connolly": 13, "A man": 4})
    assert output == "The referee who gave the least fouls in the 2021/22 season was: A man with a total fouls given of 4"
    assert type(output) == str

def test_ref_with_highest_average_of_fouls_given_per_game():
    output = ref_with_highest_average_of_fouls_given_per_game({"B connolly": 13.45, "A man": 4.3})
    assert output == "The referee who had the highest average of fouls given per game in the 2021/22 season was: B connolly with an average fouls per game of 13.45 "
    assert type(output) == str

def test_ref_with_lowest_average_of_fouls_given_per_game():
    output = ref_with_lowest_average_of_fouls_given_per_game({"B connolly": 13.45, "A man": 4.3})
    assert output == "The referee who had the lowest average of fouls given per game in the 2021/22 season was: A man with an average fouls per game of 4.3 "
    assert type(output) == str

if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data from csv and split into lists
    read_data_and_create_lists()
    pytest.main(["test_dictionary_calculations.py", "-vv"])