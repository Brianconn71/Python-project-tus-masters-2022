from main import *
import pydoc

total_referees_data = {}
refs_with_count_of_games = {}

def get_list_of_refs_and_occurances_in_data(referees):
    unique_values = set(referees)
    num_of_games_reffed = [referees.count(value) for value in unique_values]
    for ref , count in zip(referees, num_of_games_reffed):
        refs_with_count_of_games[ref] = count

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

def ref_with_highest_average_of_fouls_given_per_game(referees_data: dict):
    ref_with_most_fouls = max(referees_data, key=referees_data.get)
    print(f"The referee who gave the most fouls in the 2021/22 season was: {ref_with_most_fouls}")

def ref_with_lowest_average_of_fouls_given_per_game(referees_data: dict):
    ref_with_most_fouls = max(referees_data, key=referees_data.get)
    print(f"The referee who gave the most fouls in the 2021/22 season was: {ref_with_most_fouls}")


if __name__ == "__main__":
    read_data_and_create_lists()
    total_fouls_per_game = get_total_fouls_per_game_in_season()
    get_list_of_refs_and_occurances_in_data(referees)
    distinct_sub_categories(referees, total_fouls_per_game)
    ref_with_most_fouls_given(total_referees_data)
    ref_with_least_fouls_given(total_referees_data)
    ref_with_highest_average_of_fouls_given_per_game(total_referees_data)