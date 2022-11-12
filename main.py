import pydoc
import matplotlib.pyplot as plt


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


def read_data_and_create_lists():
    """
    Reads the data from the csv file in data folder and adds data to lists.
    """
    
    # Open the data in the correct folder
    with open("/home/briancon71/scripting/Assignment/data/Ref Data.csv", "r") as data_file:
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
            
            referees.append(referee)
            full_time_results.append(full_time_result)
            half_time_results.append(half_time_result)
            full_time_home_goals.append(int(full_time_home_goal))
            full_time_away_goals.append(int(full_time_away_goal))
            half_time_home_goals.append(int(half_time_home_goal))
            half_time_away_goals.append(int(half_time_away_goal))
            home_fouls.append(int(home_foul))
            away_fouls.append(int(away_foul))
            home_yellows.append(int(home_yellow))
            away_yellows.append(int(away_yellow))
            home_reds.append(int(home_red))
            away_reds.append(int(away_red))


def get_number_of_games_in_season():
    """
    gets the total number of matches in the season.
    
    I am using a function to get the length of the home_fouls list based on the assumption that a match will always have at least one home_foul per game
    """    
    games_in_season = len(home_fouls)
    get_average_fouls_per_game(games_in_season)

def get_total_fouls_per_game_in_season():
    """
    This function calculates the total fouls per game over the course of the season
    """    
    total_fouls_per_game_in_season = []
    for home,away in zip(home_fouls, away_fouls):
        fouls = home + away
        total_fouls_per_game_in_season.append(fouls)
    get_median_fouls_per_game(total_fouls_per_game_in_season)
    get_mode_fouls_per_game(total_fouls_per_game_in_season)
    max_fouls = get_maximum_fouls_in_a_game(total_fouls_per_game_in_season)
    min_fouls = get_minimum_fouls_in_a_game(total_fouls_per_game_in_season)
    get_range_of_fouls(max_fouls, min_fouls)
    get_interquartile_range_of_fouls(total_fouls_per_game_in_season)


def get_average_fouls_per_game(total_games):
    """
    Takes in the total games in a season and uses this as the divisor in the equation to get the average fouls per game which is a total of home fouls + away fouls and divided.
    
    This is then rounded to two decimal places

    Args:
        total_games (int): total games in season which was obtained in the get_number_of_games_in_season function
    """
    total_home_fouls = sum(home_fouls)
    total_away_fouls = sum(away_fouls)
    
    total_fouls_in_season = (total_home_fouls + total_away_fouls) / total_games
    
    total_fouls_rounded = round(total_fouls_in_season, 2)
    
    print(f"The average number of fouls per game for the 2021/22 season was {total_fouls_rounded} fouls")
    return total_fouls_rounded

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
    
    print(f"The median number of fouls per game over the course of the 21/22 season is: {median_value:.1f}")
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
    print(f"The mode number of fouls per game over the course of the 21/22 season is: {mode_value}")
    return mode_value


def get_maximum_fouls_in_a_game(total_fouls):
    """
    This function gets the maximum value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing the total number of fouls per game over the season. will contain 380 values
    """    
    max_fouls = max(total_fouls)
    print(f"The maximum number of fouls in a game over the course of the 21/22 season was: {max_fouls}")
    return max_fouls

def get_minimum_fouls_in_a_game(total_fouls):
    """
    This function gets the minimum value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing the total number of fouls per game over the season. will contain 380 values
    """    
    min_fouls = min(total_fouls)
    print(f"The minimum number of fouls in a game over the course of the 21/22 season was: {min_fouls}")
    return min_fouls

def get_range_of_fouls(max_fouls, min_fouls):
    print(f"The range of fouls in a game over the course of the 21/22 season was: {min_fouls}, {max_fouls}")

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
    
    print(f"The interquartile range of fouls in a game over the course of the 21/22 season was: {interquartile_range}")

def get_standard_deviation_of_fouls(x,total_games):
    mean = get_average_fouls_per_game(total_games)
    total = 0
    for game in x:
        new_number = game - mean
        new_number_squared = new_number ** 2
        total += new_number_squared
    divide_by_length = total / (len(x) - 1)
    standard_dev = divide_by_length ** (1/2)
    
    print(f"The standard deviation of fouls in a game over the course of the 21/22 season was: {standard_dev}")
    return standard_dev

def get_pearson_mode_skewness_of_fouls(total_games, x):
    mean = get_average_fouls_per_game(total_games)
    mode = get_mode_fouls_per_game(x)
    standard_dev = get_standard_deviation_of_fouls(x , total_games)
    
    pearson_skew = (mean - mode) / standard_dev
    
    print(f"The Pearson Mode Skewness of fouls in a game over the course of the 21/22 season was: {pearson_skew}")
    return pearson_skew


def get_alternative_pearson_mode_skewness_of_fouls(total_games, x):
    mean = get_average_fouls_per_game(total_games)
    mode = get_mode_fouls_per_game(x)
    standard_dev = get_standard_deviation_of_fouls(x, total_games)
    
    alternative_pearson_skew = 3 * (mean - mode) / standard_dev
    
    print(f"The Alternative Pearson Mode Skewness of fouls in a game over the course of the 21/22 season was: {alternative_pearson_skew}")
    return alternative_pearson_skew

def get_correlation_of_fouls(max_fouls, min_fouls):
    pass
    


# matplotlib stuff
# plt.plot(x,y)
# plt.show()


if __name__ == "__main__":
    read_data_and_create_lists()
    get_number_of_games_in_season()
    get_total_fouls_per_game_in_season()
    games_in_season = len(home_fouls)
    total_fouls_per_game_in_season = []
    for home,away in zip(home_fouls, away_fouls):
        fouls = home + away
        total_fouls_per_game_in_season.append(fouls)
    get_standard_deviation_of_fouls(total_fouls_per_game_in_season, games_in_season)
    get_pearson_mode_skewness_of_fouls(games_in_season, total_fouls_per_game_in_season)
    get_alternative_pearson_mode_skewness_of_fouls(games_in_season, total_fouls_per_game_in_season)