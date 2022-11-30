import pydoc
import matplotlib.pyplot as plt
import unittest


# initializing the lists globally for use with entire file.
referees = []
full_time_home_goals = []
full_time_away_goals = []
half_time_home_goals = []
half_time_away_goals = []
full_time_results = []
half_time_results = []
home_fouls = []
away_fouls = []
home_yellows = []
away_yellows = []
home_reds = []
away_reds = []


# read in data and append data from csv to the lists above
def read_data_and_create_lists():
    """
    Reads the data from the csv file in data folder and adds data to lists.
    """
    
    # Open the data in the correct folder
    with open("data/Ref Data.csv", "r") as data_file:
        # remove the headers from the data
        headers = data_file.readline()
        # loop through the lines of data in the file
        for data in data_file:
            # splittind data into lists
            (referee, full_time_home_goal, full_time_away_goal,
            full_time_result, half_time_home_goal, half_time_away_goal,
            half_time_result, home_foul, away_foul, home_yellow, away_yellow,
            home_red, away_red) = data.split(
                ",")
            
            #appending data to referees list
            referees.append(referee)
            #appending data to full_time_results list
            full_time_results.append(full_time_result)
            #appending data to half_time_results list
            half_time_results.append(half_time_result)
            #appending data to full_time__home_goals list
            full_time_home_goals.append(int(full_time_home_goal))
            #appending data to full_time__away_goals list
            full_time_away_goals.append(int(full_time_away_goal))
            #appending data to half_time__home_goals list
            half_time_home_goals.append(int(half_time_home_goal))
            #appending data to half_time__away_goals list
            half_time_away_goals.append(int(half_time_away_goal))
            #appending data to home_fouls list
            home_fouls.append(int(home_foul))
            #appending data to away_fouls list
            away_fouls.append(int(away_foul))
            #appending data to home_yellows list
            home_yellows.append(int(home_yellow))
            #appending data to away_yellows list
            away_yellows.append(int(away_yellow))
            #appending data to home_reds list
            home_reds.append(int(home_red))
            #appending data to away_reds list
            away_reds.append(int(away_red))


def get_number_of_games_in_season():
    """
    gets the total number of matches in the season.
    
    I am using a function to get the length of the home_fouls list based on the assumption that a match will always have at least one home_foul per game
    """    
    # get the length of home fouls list as a means of getting total gamies in the season as each game contains one or more home fouls
    games_in_season = len(home_fouls)
    # calling the get average fouls function to use games_in_season as an argument as it will be an int value of amount of games in the season
    get_average_fouls_per_game(games_in_season)

def get_total_fouls_per_game_in_season():
    """
    This function calculates the total fouls per game over the course of the season
    """    
    # initialize empty list
    total_fouls_per_game_in_season = []
    # zip home and away fouls and loop through
    for home,away in zip(home_fouls, away_fouls):
        # Calculate total fouls pergame by adding home and away fouls for each game to get total
        fouls = home + away
        # appending the above calculation to empty list
        total_fouls_per_game_in_season.append(fouls)
    # using the list of total fouls to calculate the median fouls per game
    get_median_fouls_per_game(total_fouls_per_game_in_season)
    # using the list of total fouls to calculate the mode fouls per game
    get_mode_fouls_per_game(total_fouls_per_game_in_season)
    # using the list of total fouls to calculate the maximum fouls per game
    max_fouls = get_maximum_fouls_in_a_game(total_fouls_per_game_in_season)
    # using the list of total fouls to calculate the minimum fouls per game
    min_fouls = get_minimum_fouls_in_a_game(total_fouls_per_game_in_season)
    get_range_of_fouls(max_fouls, min_fouls)
    # using the list of total fouls to calculate the interquartile range of fouls per game
    get_interquartile_range_of_fouls(total_fouls_per_game_in_season)
    # returns the list of total fouls per game
    return total_fouls_per_game_in_season


def get_average_fouls_per_game(total_games):
    """
    Takes in the total games in a season and uses this as the divisor in the equation to get the average fouls per game which is a total of home fouls + away fouls and divided.
    
    This is then rounded to two decimal places

    Args:
        total_games (int): total games in season which was obtained in the get_number_of_games_in_season function
    """
    total_home_fouls = sum(home_fouls)
    total_away_fouls = sum(away_fouls)
    
    average_fouls_in_season = (total_home_fouls + total_away_fouls) / total_games
    
    average_fouls_rounded = round(average_fouls_in_season, 2)
    return average_fouls_rounded

def test_get_average_fouls_per_game():
    assert get_average_fouls_per_game(380) == 78

def get_median_fouls_per_game(total_fouls):
    """
    This function calculates the median number of fouls per game over the season

    Args:
        total_fouls (list[int]): A list of integers which show total number of fouls per game over the season.
    """    
    sorted_list_fouls_per_game = sorted(total_fouls)
    middle_value = int(len(sorted_list_fouls_per_game) / 2)
    if len(sorted_list_fouls_per_game) % 2 == 1:
        median_value = sorted_list_fouls_per_game[middle_value]
    else:
        median_value = ((sorted_list_fouls_per_game[middle_value - 1] + sorted_list_fouls_per_game[middle_value]) / 2)
    
    return median_value


def get_mode_fouls_per_game(total_fouls):
    """
    This function gets the mode value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing the total number of fouls per game over the season. will contain 380 values
    """    
    unique_values = sorted(set(total_fouls))
    times_in_list = [total_fouls.count(value) for value in unique_values]
    max_value = max(times_in_list)
    index_of_max = times_in_list.index(max_value)
    mode_value = unique_values[index_of_max]
    return mode_value


def get_maximum_fouls_in_a_game(total_fouls):
    """
    This function gets the maximum value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing the total number of fouls per game over the season. will contain 380 values
    """    
    max_fouls = max(total_fouls)
    return max_fouls

def get_minimum_fouls_in_a_game(total_fouls):
    """
    This function gets the minimum value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing the total number of fouls per game over the season. will contain 380 values
    """    
    min_fouls = min(total_fouls)
    return min_fouls

def get_range_of_fouls(max_fouls, min_fouls):
    range = f"{min_fouls}, {max_fouls}"
    return range

def get_interquartile_range_of_fouls(total_games):
    sorted_list = sorted(total_games)
    middle_number = int(len(sorted_list) / 2)
    if len(sorted_list) % 2 == 1:
        lower_half = sorted_list[:middle_number]
        upper_half = sorted_list[middle_number + 1:]
    else:
        lower_half = sorted_list[:middle_number]
        upper_half = sorted_list[middle_number:]
    lower_half_median = get_median_fouls_per_game(lower_half)
    upper_half_median = get_median_fouls_per_game(upper_half)
    
    interquartile_range = upper_half_median - lower_half_median
    
    return interquartile_range

def get_standard_deviation_of_fouls(x,total_games):
    mean = get_average_fouls_per_game(total_games)
    total = 0
    for game in x:
        new_number = game - mean
        new_number_squared = new_number ** 2
        total += new_number_squared
    divide_by_length = total / (len(x) - 1)
    standard_dev = divide_by_length ** (1/2)
    
    return standard_dev

def get_pearson_mode_skewness_of_fouls(total_games, x):
    mean = get_average_fouls_per_game(total_games)
    mode = get_mode_fouls_per_game(x)
    standard_dev = get_standard_deviation_of_fouls(x , total_games)
    
    pearson_skew = (mean - mode) / standard_dev
    
    return pearson_skew


def get_alternative_pearson_mode_skewness_of_fouls(total_games, x):
    mean = get_average_fouls_per_game(total_games)
    mode = get_mode_fouls_per_game(x)
    standard_dev = get_standard_deviation_of_fouls(x, total_games)
    
    alternative_pearson_skew = 3 * (mean - mode) / standard_dev
    
    return alternative_pearson_skew

def get_covariance_between_datasets(home_fouls, away_fouls):
    home_mean = sum(home_fouls) / len(home_fouls)
    away_mean = sum(away_fouls) / len(away_fouls)
    t = []
    for x, y in zip(home_fouls, away_fouls):
        t.append((x - home_mean) * (y - away_mean))
    d = sum(t)
    co_var = d / (len(home_fouls) - 1)
    return co_var
    

def get_correlation_of_fouls(home_fouls, away_fouls):
    g = get_covariance_between_datasets(home_fouls, away_fouls)
    bh = home_fouls + away_fouls
    bhh = len(bh)
    f = get_standard_deviation_of_fouls(home_fouls, bhh)
    p = get_standard_deviation_of_fouls(away_fouls, bhh)
    correlation = g / (f * g)
    return correlation
