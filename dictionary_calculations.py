from calculations import *
from dictionary_visualisations import *
import pydoc

total_referees_data = {}
num_of_games_reffed = {}
ref_with_avg_value = {}

def get_dict_of_refs_and_occurances_in_data(referees):
    """
    gets the list of referees, counts its occuraancws in the list and adds the values to a dictionary

    Args:
        referees (list[str]): list of strings

    Returns:
        num_of_games_reffed (Dict): dictionary of unique referees and how often they have reffed games
    """    
    unique_values = set(referees)
    for value in unique_values:
        num_of_games_reffed[value] = referees.count(value)
    return num_of_games_reffed

def get_total_refs_data(ref_data, total_fouls_per_game):
    """
    takes in a list of referees and a list of integers with total fouls and returns a dictionary with
    referees as keys and the total fouls they gave over the season as the values

    Args:
        ref_data (list[str]): list of strings
        total_fouls_per_game (list[int]): list of integers

    Returns:
        total_referees_data (dict): dictionary of unique referees total fouls given over season
    """    
    for ref , fouls_in_game in zip(ref_data, total_fouls_per_game):
        total_referees_data[ref] = total_referees_data.get(ref,0) + fouls_in_game
    return total_referees_data

def distinct_sub_categories(total_referees_data):
    """
    This fucntion will take in a dictionary of referees data and gets the len of the dict.keys()
    to return distict number of referees

    Args:
        total_referees_data (dict): dictionary of referees and total fouls given

    Returns:
        number_of_referees (int): distinct number of referees
    """    
    number_of_referees = len(total_referees_data.keys())
    print(f"The distinct number of referees is: {number_of_referees}")
    return number_of_referees

def dict_from_average_fouls_per_game(referees_data: dict, num_of_games_reffed: dict):
    """
    takes in two dictionaries representing refereed data and returns a new dict
    with the referee and average fouls given by each referee

    Args:
        referees_data (dict): dictionary of referees and total fouls given
        num_of_games_reffed (dict): dictionary of referees and number of games referred

    Returns:
        ref_with_avg_value (dict): a new dictionary with referees and their average fouls given over the season
    """    
    for ref, fouls in referees_data.items():
        if ref in num_of_games_reffed.keys():
            average_value = round(fouls / num_of_games_reffed[ref], 2)
            ref_with_avg_value[ref] = average_value
    ref_with_highest_average_of_fouls_given_per_game(ref_with_avg_value)
    ref_with_lowest_average_of_fouls_given_per_game(ref_with_avg_value)
    return ref_with_avg_value

def ref_with_most_fouls_given(referees_data):
    """
    Gets the ref  who gave most fouls in 21/22 by taking the max value from a dictionary
    displaying ref data and total fouls given by each

    Args:
        referees_data (dict): dictionary of referees and total fouls given

    Returns:
        ref_with_most_fouls (str): string value of ref who gave most fouls
    """    
    ref_with_most_fouls = max(referees_data, key=referees_data.get)
    num_of_fouls_given = max(referees_data.values())
    ref_with_most_fouls = f"The referee who gave the most fouls in the 2021/22 season was: {ref_with_most_fouls} with a total fouls given of {num_of_fouls_given}"
    return ref_with_most_fouls

def ref_with_least_fouls_given(referees_data):
    """
    Gets the ref  who gave least fouls in 21/22 by taking the min value from a dictionary
    displaying ref data and total fouls given by each

    Args:
        referees_data (dict): dictionary of referees and total fouls given

    Returns:
        ref_with_least_fouls (str): string value of ref who gave least fouls
    """    
    ref_with_least_fouls = min(referees_data, key=referees_data.get)
    num_of_fouls_given = min(referees_data.values())
    ref_with_least_fouls = f"The referee who gave the least fouls in the 2021/22 season was: {ref_with_least_fouls} with a total fouls given of {num_of_fouls_given}"
    return ref_with_least_fouls

def ref_with_highest_average_of_fouls_given_per_game(ref_with_avg_value):
    """
    Gets the ref  who gave highest average of fouls in 21/22 by taking the value from a dictionary
    displaying ref data and average given by each

    Args:
        ref_with_avg_value (dict): dictionary of referees and average fouls given per game

    Returns:
        highest_avg_value (str): string value of ref had the highest avergae of fouls per game
    """    
    ref_with_highest_average = max(ref_with_avg_value, key=ref_with_avg_value.get)
    highest_average = ref_with_avg_value[ref_with_highest_average]
    highest_avg_value = f"The referee who had the highest average of fouls given per game in the 2021/22 season was: {ref_with_highest_average} with an average fouls per game of {highest_average} "
    return highest_avg_value
    

def ref_with_lowest_average_of_fouls_given_per_game(ref_with_avg_value):
    """
    Gets the ref  who gave lowest average of fouls in 21/22 by taking the value from a dictionary
    displaying ref data and average given by each

    Args:
        ref_with_avg_value (dict): dictionary of referees and average fouls per game

    Returns:
        lowest_average_value (str): string value of ref had the lowest avergae of fouls per game
    """    
    ref_with_lowest_average = min(ref_with_avg_value, key=ref_with_avg_value.get)
    lowest_average = ref_with_avg_value[ref_with_lowest_average]
    lowest_average_value = f"The referee who had the lowest average of fouls given per game in the 2021/22 season was: {ref_with_lowest_average} with an average fouls per game of {lowest_average} "
    return lowest_average_value
