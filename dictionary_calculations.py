from calculations import *
from dictionary_visualisations import *
import pydoc

total_referees_data = {}
num_of_games_reffed = {}
new_dict = {}

def get_dict_of_refs_and_occurances_in_data(referees):
    unique_values = set(referees)
    for value in unique_values:
        num_of_games_reffed[value] = referees.count(value)
    return num_of_games_reffed

def get_total_refs_data(ref_data, total_fouls_per_game):
    for ref , fouls_in_game in zip(ref_data, total_fouls_per_game):
        total_referees_data[ref] = total_referees_data.get(ref,0) + fouls_in_game
    return total_referees_data

def distinct_sub_categories(total_referees_data):
    number_of_referees = len(total_referees_data.keys())
    print(f"The distinct number of referees is: {number_of_referees}")
    return number_of_referees

def dict_from_average_fouls_per_game(referees_data: dict, num_of_games_reffed: dict):
    for ref, fouls in referees_data.items():
        if ref in num_of_games_reffed.keys():
            average_value = round(fouls / num_of_games_reffed[ref], 2)
            new_dict[ref] = average_value
    ref_with_highest_average_of_fouls_given_per_game(new_dict)
    ref_with_lowest_average_of_fouls_given_per_game(new_dict)
    return new_dict

def ref_with_most_fouls_given(referees_data):
    ref_with_most_fouls = max(referees_data, key=referees_data.get)
    return ref_with_most_fouls

def ref_with_least_fouls_given(referees_data):
    ref_with_least_fouls = min(referees_data, key=referees_data.get)
    return ref_with_least_fouls

def ref_with_highest_average_of_fouls_given_per_game(ref_with_avg_value):
    ref_with_highest_average = max(ref_with_avg_value, key=ref_with_avg_value.get)
    highest_average = ref_with_avg_value[ref_with_highest_average]
    highest_avg_value = f"The referee who had the highest average of fouls given per game in the 2021/22 season was: {ref_with_highest_average} with an average fouls per game of {highest_average} "
    return highest_avg_value
    

def ref_with_lowest_average_of_fouls_given_per_game(ref_with_avg_value):
    ref_with_lowest_average = min(ref_with_avg_value, key=ref_with_avg_value.get)
    lowest_average = ref_with_avg_value[ref_with_lowest_average]
    lowest_average_value = f"The referee who had the lowest average of fouls given per game in the 2021/22 season was: {ref_with_lowest_average} with an average fouls per game of {lowest_average} "
    return lowest_average_value
