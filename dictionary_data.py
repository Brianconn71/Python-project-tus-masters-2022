from main import *
import pydoc

total_referees_data = {}
num_of_games_reffed = {}

def get_dict_of_refs_and_occurances_in_data(referees):
    unique_values = set(referees)
    for value in unique_values:
        num_of_games_reffed[value] = referees.count(value)
    return num_of_games_reffed

def distinct_sub_categories(ref_data, total_fouls_per_game):
    # referees_data[referees_data]
    for ref , fouls_in_game in zip(ref_data, total_fouls_per_game):
        total_referees_data[ref] = total_referees_data.get(ref,0) + fouls_in_game
    number_of_referees = len(total_referees_data.keys())
    print(f"The distinct number of referees is: {number_of_referees}")
    return number_of_referees

def ref_with_most_fouls_given(referees_data: dict):
    ref_with_most_fouls = max(referees_data, key=referees_data.get)
    print(f"The referee who gave the most fouls in the 2021/22 season was: {ref_with_most_fouls}")

def ref_with_least_fouls_given(referees_data: dict):
    ref_with_least_fouls = min(referees_data, key=referees_data.get)
    print(f"The referee who gave the least fouls in the 2021/22 season was: {ref_with_least_fouls}")

def ref_with_highest_average_of_fouls_given_per_game(referees_data: dict, num_of_games_reffed: dict):
    ref_with_avg_value_dict = {}
    for ref, fouls in referees_data.items():
        if ref in num_of_games_reffed.keys():
            average_value = round(fouls / num_of_games_reffed[ref], 2)
            ref_with_avg_value_dict[ref] = average_value
    ref_with_highest_average = max(ref_with_avg_value_dict, key=ref_with_avg_value_dict.get)
    highest_average_value = ref_with_avg_value_dict[ref_with_highest_average]
    print(f"The referee who had the highest average of fouls given per game in the 2021/22 season was: {ref_with_highest_average} with an average fouls per game of {highest_average_value} ")
    ref_with_lowest_average_of_fouls_given_per_game(ref_with_avg_value_dict)

def ref_with_lowest_average_of_fouls_given_per_game(ref_with_avg_value):
    ref_with_lowest_average = min(ref_with_avg_value, key=ref_with_avg_value.get)
    lowest_average_value = ref_with_avg_value[ref_with_lowest_average]
    print(f"The referee who had the lowest average of fouls given per game in the 2021/22 season was: {ref_with_lowest_average} with an average fouls per game of {lowest_average_value} ")


if __name__ == "__main__":
    read_data_and_create_lists()
    total_fouls_per_game = get_total_fouls_per_game_in_season()
    get_dict_of_refs_and_occurances_in_data(referees)
    distinct_sub_categories(referees, total_fouls_per_game)
    ref_with_most_fouls_given(total_referees_data)
    ref_with_least_fouls_given(total_referees_data)
    ref_with_highest_average_of_fouls_given_per_game(total_referees_data, num_of_games_reffed)