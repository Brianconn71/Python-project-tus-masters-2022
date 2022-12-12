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

filename = "data/Ref_data.csv"


# read in data and append data from csv to the lists above
def read_data_and_create_lists():
    """
    Reads the data from the csv file in data folder and adds data to lists.
    """    
    try:
        # Open the data in the correct folder
        with open(filename, "r") as data_file:
            try:
                # remove the headers from the data
                headers = data_file.readline()
            except ValueError:
                print(f"{data_file} not in correct format")
            # loop through the lines of data in the file
            for data in data_file:
                try:
                    # splittind data into lists
                    (referee, full_time_home_goal, full_time_away_goal,
                    full_time_result, half_time_home_goal, half_time_away_goal,
                    half_time_result, home_foul, away_foul, home_yellow, away_yellow,
                    home_red, away_red) = data.split(
                        ",")
                except ValueError:
                    print(f"{data} not in correct format")
                    continue
                
                try:
                    #appending data to referees list
                    referees.append(referee)
                except ValueError:
                    print(f"{referee} not in correct format")
                    continue
                try:
                    #appending data to full_time_results list
                    full_time_results.append(full_time_result)
                except ValueError:
                    print(f"{full_time_result} not in correct format")
                    continue
                try:
                    #appending data to half_time_results list
                    half_time_results.append(half_time_result)
                except ValueError:
                    print(f"{half_time_result} could not be converted to an integer")
                    continue
                try:
                    #appending data to full_time__home_goals list
                    full_time_home_goals.append(int(full_time_home_goal))
                except ValueError:
                    print(f"{full_time_home_goal} could not be converted to an integer")
                    continue
                try:
                    #appending data to full_time__away_goals list
                    full_time_away_goals.append(int(full_time_away_goal))
                except ValueError:
                    print(f"{full_time_away_goal} could not be converted to an integer")
                    continue
                try:
                    #appending data to half_time__home_goals list
                    half_time_home_goals.append(int(half_time_home_goal))
                except ValueError:
                    print(f"{half_time_home_goal} could not be converted to an integer")
                    continue
                try:
                    #appending data to half_time__away_goals list
                    half_time_away_goals.append(int(half_time_away_goal))
                except ValueError:
                    print(f"{half_time_away_goal} could not be converted to an integer")
                    continue
                try:
                    #appending data to home_fouls list
                    home_fouls.append(int(home_foul))
                except ValueError:
                    print(f"{home_foul} could not be converted to an integer")
                    continue
                try:
                    #appending data to away_fouls list
                    away_fouls.append(int(away_foul))
                except ValueError:
                    print(f"{away_foul} could not be converted to an integer")
                    continue
                try:
                    #appending data to home_yellows list
                    home_yellows.append(int(home_yellow))
                except ValueError:
                    print(f"{home_yellow} could not be converted to an integer")
                    continue
                try:
                    #appending data to away_yellows list
                    away_yellows.append(int(away_yellow))
                except ValueError:
                    print(f"{away_yellow} could not be converted to an integer")
                    continue
                try:
                    #appending data to home_reds list
                    home_reds.append(int(home_red))
                except ValueError:
                    print(f"{home_red} could not be converted to an integer")
                    continue
                try:
                    #appending data to away_reds list
                    away_reds.append(int(away_red))
                except ValueError:
                    print(f"{away_red} could not be converted to an integer")
                    continue
    except FileNotFoundError:
        print(f"{filename} does not exist")


def get_number_of_games_in_season():
    """
    gets the total number of matches in the season.
    
    I am using a function to get the length of the home_fouls list based on the assumption that a match will always have at least one home_foul per game

    Returns:
        games_in_season (int): the value indicating the total number of games in the season
    """   
    # get the length of home fouls list as a means of getting total gamies in the season as each game contains one or more home fouls
    games_in_season = len(home_fouls)
    # calling the get average fouls function to use games_in_season as an argument as it will be an int value of amount of games in the season
    get_average_fouls_per_game(games_in_season)
    # returns the total number of games in the season
    return games_in_season

def get_total_fouls_per_game_in_season():
    """
    This function calculates the total fouls per game over the course of the season

    Returns:
        total_fouls_per_game_in_season (list[int]): list of the total fouls per game for the season
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
        total_games (list[int]): total games in season which was obtained in the get_number_of_games_in_season function

    Returns:
        average_fouls_rounded (float): the float value of the average value of the lists correct to two decimal places
    """
    total_home_fouls = sum(home_fouls)
    total_away_fouls = sum(away_fouls)
    
    try:
        average_fouls_in_season = (total_home_fouls + total_away_fouls) / total_games
        average_fouls_rounded = round(average_fouls_in_season, 2)
        return average_fouls_rounded
    except ZeroDivisionError:
        print(f"total games list is empty, cannot divide by zero")

def get_median_fouls_per_game(total_fouls):
    """
    This function calculates the median number of fouls per game over the season

    Args:
        total_fouls (list[int]): A list of integers which show total number of fouls per game over the season.

    Returns:
        median_value (int): the integer value of the value which appears as the middle value in the list
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

    Returns:
        mode_value (int): the integer value of the value which appears most often in the data
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

    Returns:
        max_fouls (int): the integer value of hoghest value in the list.
    """    
    max_fouls = max(total_fouls)
    return max_fouls

def get_minimum_fouls_in_a_game(total_fouls):
    """
    This function gets the minimum value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing the total number of fouls per game over the season. will contain 380 values

    Returns:
        min_fouls (int): the integer value of lowest value in the list.
    """    
    min_fouls = min(total_fouls)
    return min_fouls

def get_range_of_fouls(max_fouls, min_fouls):
    """
    Get the range of fouls by subtracting max foul by min foul

    Args:
        max_fouls (int): takes in the value of the maximum foul
        min_fouls (int): takes in the vaue of the minimum foul

    Returns:
        range (str): returns a formatted string indicating the range of values
    """    
    range = f"{min_fouls}, {max_fouls}"
    return range

def get_interquartile_range_of_fouls(total_fouls_per_game):
    """
    Get the interquartile range from list of integers

    Args:
        total_fouls_per_game (list[int]): list of integers to calculate interquartile range from

    Returns:
        interquartile_range: interquartile range for the list of integers.
    """    
    sorted_list = sorted(total_fouls_per_game)
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

def get_standard_deviation_of_fouls(total_fouls_per_game,total_games):
    """
    Get the Standard deviation from the data using a list of integers and total number of games in the season

    Args:
        total_fouls_per_game (list[int]): list of integers to calculate standard deviation from
        total_games (int): the total number of games in the season

    Returns:
        standard_dev: The standard deviation of the data
    """    
    mean = get_average_fouls_per_game(total_games)
    total = 0
    for game in total_fouls_per_game:
        new_number = game - mean
        new_number_squared = new_number ** 2
        total += new_number_squared
    divide_by_length = total / (len(total_fouls_per_game) - 1)
    standard_dev = divide_by_length ** (1/2)
    
    return standard_dev

def get_pearson_mode_skewness_of_fouls(total_games, total_fouls_per_game):
    """
    Get the pearson mode Skewness of the data 

    Args:
        total_fouls_per_game (list[int]): list of integers to calculate pearson mode Skewness from
        total_games (int): the total number of games in the season

    Returns:
        pearson_skew: the pearson mode skewness of the data
    """    
    mean = get_average_fouls_per_game(total_games)
    mode = get_mode_fouls_per_game(total_fouls_per_game)
    standard_dev = get_standard_deviation_of_fouls(total_fouls_per_game , total_games)
    
    pearson_skew = (mean - mode) / standard_dev
    
    return pearson_skew


def get_alternative_pearson_mode_skewness_of_fouls(total_games, total_fouls_per_game):
    """
    Get the alternative pearson mode skewness from the data

    Args:
        total_fouls_per_game (list[int]): list of integers to calculate alternative pearson mode from
        total_games (int): the total number of games in the season

    Returns:
        alternative_pearson_skew: the alternative pearson mode skewness from the data
    """    
    mean = get_average_fouls_per_game(total_games)
    mode = get_mode_fouls_per_game(total_fouls_per_game)
    standard_dev = get_standard_deviation_of_fouls(total_fouls_per_game, total_games)
    
    alternative_pearson_skew = 3 * (mean - mode) / standard_dev
    
    return alternative_pearson_skew

def get_covariance_between_datasets(home_fouls, away_fouls):
    """
    Gets the covariance between ywo lists of integers from the data

    Args:
        home_fouls (list[int]): list of integers containing home fouls per game per season
        away_fouls (list[int]): list of integers containing away fouls per game per season

    Returns:
        co_var: the co variance between the two lists of integers
    """    
    home_mean = sum(home_fouls) / len(home_fouls)
    away_mean = sum(away_fouls) / len(away_fouls)
    totals = []
    for home, away in zip(home_fouls, away_fouls):
        totals.append((home - home_mean) * (away - away_mean))
    total_values = sum(totals)
    co_var = total_values / (len(home_fouls) - 1)
    return co_var
    

def get_correlation_of_fouls(home_fouls, away_fouls):
    """
    Gets the correlation between two lists of integers from the data

    Args:
        home_fouls (list[int]): list of integers containing home fouls per game per season
        away_fouls (list[int]): list of integers containing away fouls per game per season

    Returns:
        correlation: the correlation between the two lists.
    """    
    home_avg = sum(home_fouls) / len(home_fouls)
    away_avg = sum(away_fouls) / len(away_fouls)
    mean_diff_home = []
    mean_diff_away = []
    for home_foul, away_foul in zip(home_fouls, away_fouls):
        mean_diff_home.append(home_foul-home_avg)
        mean_diff_away.append(away_foul-away_avg)
    home_sqr_list = []
    away_sqr_list = []
    diff = []
    for home_diff, away_diff in zip(mean_diff_home, mean_diff_away):
        home_sqr_list.append(home_diff*home_diff)
        away_sqr_list.append(away_diff*away_diff)
        diff.append(home_diff*away_diff)
    correlation= sum(diff)/ ((sum(home_sqr_list) * sum(away_sqr_list)) ** 0.5)
    return correlation
