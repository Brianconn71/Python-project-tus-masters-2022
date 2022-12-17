# Student ID: A00204916
"""
This file is used define the functions used in the project
"""
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
    # tries to open correct file
    try:
        # setting the csv to be read as a variable
        filename = "data/Ref_data.csv"
        # Open the data in the correct folder
        with open(filename, "r") as data_file:
            # tries to reader headers in csv
            try:
                # remove the headers from the data
                _ = data_file.readline()
            # catches error if data not correct format
            except ValueError:
                # prints error to console
                print(f"{data_file} not in correct format")
            # loop through the lines of data in the file
            for data in data_file:
                # tries to split data into correct compnents
                try:
                    # splittind data into lists
                    (referee, full_time_home_goal, full_time_away_goal,
                        full_time_result, half_time_home_goal,
                        half_time_away_goal, half_time_result, home_foul,
                        away_foul, home_yellow, away_yellow,
                        home_red, away_red) = data.split(
                        ",")
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{data} not in correct format")
                # tries to append correct data to correct list
                try:
                    # appending data to referees list
                    referees.append(referee)
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{referee} not in correct format")
                # tries to append correct data to correct list
                try:
                    # appending data to full_time_results list
                    full_time_results.append(full_time_result)
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{full_time_result} not in correct format")
                # tries to append correct data to correct list
                try:
                    # appending data to half_time_results list
                    half_time_results.append(half_time_result)
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{half_time_result} "
                          f"could not be converted to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to full_time__home_goals list
                    full_time_home_goals.append(int(full_time_home_goal))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{full_time_home_goal} "
                          f"could not be converted to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to full_time__away_goals list
                    full_time_away_goals.append(int(full_time_away_goal))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{full_time_away_goal} "
                          f"could not be converted to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to half_time__home_goals list
                    half_time_home_goals.append(int(half_time_home_goal))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{half_time_home_goal} "
                          f"could not be converted to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to half_time__away_goals list
                    half_time_away_goals.append(int(half_time_away_goal))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{half_time_away_goal} "
                          f"could not be converted to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to home_fouls list
                    home_fouls.append(int(home_foul))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{home_foul} could not be converted to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to away_fouls list
                    away_fouls.append(int(away_foul))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{away_foul} could not be converted to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to home_yellows list
                    home_yellows.append(int(home_yellow))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{home_yellow} could not be converted "
                          f"to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to away_yellows list
                    away_yellows.append(int(away_yellow))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{away_yellow} could not be converted "
                          f"to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to home_reds list
                    home_reds.append(int(home_red))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{home_red} could not be converted to an integer")
                # tries to append correct data to correct list
                try:
                    # appending data to away_reds list
                    away_reds.append(int(away_red))
                # catches error if data not correct format
                except ValueError:
                    # prints error to console
                    print(f"{away_red} could not be converted to an integer")
    # catches error if file not found
    except FileNotFoundError:
        # prints error to console
        print(f"{filename} does not exist")


def get_number_of_games_in_season(home_fouls):
    """
    gets the total number of matches in the season.

    I am using a function to get the length of the home_fouls list based on
    the assumption that a match will always have at least one
    a home_foul

    Returns:
        games_in_season (int): the value indicating the total
        number of games in the season
    """
    # get the length of home fouls list as a means of getting total games
    # in the season as each game contains one or more home fouls
    games_in_season = len(home_fouls)
    # calling the get average fouls function to use games_in_season as
    # an argument as it will be an int value of amount of games in the season
    get_average_fouls_per_game(games_in_season)
    # returns the total number of games in the season
    return games_in_season


def get_total_fouls_per_game_in_season(home_fouls, away_fouls):
    """
    This function calculates the total fouls per game over the
    course of the season

    Args:
        home_fouls (list[int]): list of integers representing home fouls
        away_fouls (list[int]): list of integers representing away fouls

    Returns:
        total_fouls_per_game_in_season (list[int]): list of the total
        fouls per game for the season
    """
    # initialize empty list
    total_fouls_per_game_in_season = []
    # zip home and away fouls and loop through
    for home, away in zip(home_fouls, away_fouls):
        # Calculate total fouls pergame by adding home and away fouls
        # for each game to get total
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
    # using the list of total fouls to calculate the interquartile range
    # of fouls per game
    get_interquartile_range_of_fouls(total_fouls_per_game_in_season)
    # returns the list of total fouls per game
    return total_fouls_per_game_in_season


def get_total_fouls_per_list(fouls):
    """
    This function calculates the total fouls per game over the
    course of the season

    Args:
        fouls (list[int]): list of integers representing fouls

    Returns:
        total_fouls (int): total value of fouls in the list
    """
    # initialize empty list
    total_fouls = sum(fouls)
    # returns the total value for fouls in the list
    return total_fouls


def get_mean_fouls_per_game(fouls):
    """
    This function calculates the mean value of the list passed to it.

    Args:
        fouls (list[int]): list of integers representing fouls

    Returns:
        mean_value (int): mean value from the list of integers passed
    """
    # get the length of the list passed
    length_of_list = len(fouls)
    # get the sum of the values of the list passed
    sum_of_values = sum(fouls)
    # declare mean value and make it equal
    # the sum of the list divided by the length of the list
    mean_value = sum_of_values / length_of_list
    # returns the mean value
    return mean_value


def get_average_fouls_per_game(total_games):
    """
    Takes in the total games in a season and uses this as the divisor in the
    equation to get the average fouls per game which is a total
    of home fouls + away fouls and divided.

    This is then rounded to two decimal places

    Args:
        total_games (list[int]): total games in season list of integers

    Returns:
        average_fouls_rounded (float): the float value of the average value
        of the lists correct to two decimal places
    """
    # gets sum of values in home_fouls list
    total_home_fouls = sum(home_fouls)
    # gets sum of values in away_fouls list
    total_away_fouls = sum(away_fouls)

    # tries to get the average fouls in season
    try:
        # gets average fols in season by adding the two
        # values above and dividing by number of games in the season.
        average_fouls_in_season = (
            (total_home_fouls + total_away_fouls) / total_games)
        # rounds value to two decimal places
        average_fouls_rounded = round(average_fouls_in_season, 2)
        # returns the average value to two decimal places
        return average_fouls_rounded
    # cataches error with lists being empty, not initialised
    except ZeroDivisionError:
        # prints error to console
        print("total games list is empty, cannot divide by zero")


def get_median_fouls_per_game(total_fouls):
    """
    This function calculates the median number of fouls per game
    over the season

    Args:
        total_fouls (list[int]): A list of integers which show total
        number of fouls per game over the season.

    Returns:
        median_value (int): the integer value of the value which
        appears as the middle value in the list
    """
    # declares a variable equal to the list passed sorted
    sorted_list_fouls_per_game = sorted(total_fouls)
    # finds the middle value in the sorted list
    middle_value = int(len(sorted_list_fouls_per_game) / 2)
    # if the list has an odd amount of values
    if len(sorted_list_fouls_per_game) % 2 == 1:
        # median is the middle value in the sorted list
        median_value = sorted_list_fouls_per_game[middle_value]
    else:
        # median value is equal to the middle value + the middle value
        # minus one divided by 2
        median_value = (
            (sorted_list_fouls_per_game[middle_value - 1] +
             sorted_list_fouls_per_game[middle_value]) / 2)

    # returns the median value
    return median_value


def get_mode_fouls_per_game(total_fouls):
    """
    This function gets the mode value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing the
        total number of fouls per game over the season.
        will contain 380 values

    Returns:
        mode_value (int): the integer value of the value which
        appears most often in the data
    """
    # find the unique values in list using set and sorting them in order.
    unique_values = sorted(set(total_fouls))
    # list comprehension to count the amount of times a
    # unique value appears in the list.
    times_in_list = [total_fouls.count(value) for value in unique_values]
    # finds the max value in the list
    max_value = max(times_in_list)
    # finds the index of the max value
    index_of_max = times_in_list.index(max_value)
    # gets the mode using the index of the list
    mode_value = unique_values[index_of_max]
    # returns the mode
    return mode_value


def get_maximum_fouls_in_a_game(total_fouls):
    """
    This function gets the maximum value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing the
        total number of fouls per game over the season.
        will contain 380 values

    Returns:
        max_fouls (int): the integer value of hoghest value in the list.
    """
    # declare a variable to equal the max value of the list passed
    max_fouls = max(total_fouls)
    # returns the max value in the list
    return max_fouls


def get_minimum_fouls_in_a_game(total_fouls):
    """
    This function gets the minimum value in the total fouls list.

    Args:
        total_fouls (list[int]): List of integers representing
        the total number of fouls per game over the season.
        will contain 380 values

    Returns:
        min_fouls (int): the integer value of lowest value in the list.
    """
    # declare a variable to equal the min value of the list passed
    min_fouls = min(total_fouls)
    # returns the min value in the list
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
    # declare a variable to equal a string value equal
    # to the min and max value passed
    range = max_fouls - min_fouls
    # returns the string value
    return range


def get_interquartile_range_of_fouls(total_fouls_per_game):
    """
    Get the interquartile range from list of integers

    Args:
        total_fouls_per_game (list[int]): list of integers to
        calculate interquartile range from

    Returns:
        interquartile_range: interquartile range for the list of integers.
    """
    # declare a variable to equal the sorted version of the list passed
    sorted_list = sorted(total_fouls_per_game)
    # finds the middle value in the sorted list
    middle_number = int(len(sorted_list) / 2)
    # if the list has an odd amount of values
    if len(sorted_list) % 2 == 1:
        # lower half is a sliced list from first value up to the mid value
        lower_half = sorted_list[:middle_number]
        # upper half is a sliced list from value after the mid
        # up to the end of the list
        upper_half = sorted_list[middle_number + 1:]
    else:
        # lower half is a sliced list from first value up to the mid value
        lower_half = sorted_list[:middle_number]
        # upper half is a sliced list from the mid value
        # up to the end of the list
        upper_half = sorted_list[middle_number:]
    # pass lower half list to the get median fouls function to
    # return the median of the list
    lower_half_median = get_median_fouls_per_game(lower_half)
    # pass upper half list to the get median fouls function to
    # return the median of the list
    upper_half_median = get_median_fouls_per_game(upper_half)

    # interquartile range formula median of upper half minus lower
    interquartile_range = upper_half_median - lower_half_median

    # returns the interquartile range
    return interquartile_range


def get_standard_deviation_of_fouls(total_fouls_per_game):
    """
    Get the Standard deviation from the data using a list of integers
    and total number of games in the season

    Args:
        total_fouls_per_game (list[int]): list of integers to
        calculate standard deviation from

    Returns:
        standard_dev: The standard deviation of the data
    """
    # mean value formula sum of list values passed
    # divided by the length of the list
    mean = sum(total_fouls_per_game) / len(total_fouls_per_game)
    # declare total to 0
    total = 0
    # loop through list
    for game in total_fouls_per_game:
        # new variable equal to each loop iteration value minus the
        # mean declared above
        new_number = game - mean
        # square the new_number
        new_number_squared = new_number ** 2
        # add all the squared numbers together on each ieration
        total += new_number_squared
    # divide the total value by the length of the list minus 1
    divide_by_length = total / (len(total_fouls_per_game) - 1)
    # find the standard deviation by getting sqrt of the division
    # value above
    standard_dev = divide_by_length ** (1/2)

    # returns the standard deviation
    return standard_dev


def get_mode_skewness_of_fouls(total_fouls_per_game):
    """
    Get the mode mode Skewness of the data

    Args:
        total_fouls_per_game (list[int]): list of integers to
        calculate mode mode Skewness from

    Returns:
        mode_skew: the mode mode skewness of the data
    """
    # mean value formula sum of list values passed
    # divided by the length of the list
    mean = sum(total_fouls_per_game) / len(total_fouls_per_game)
    # get the mode of list passed by calling the get mode fouls
    # function declared above
    mode = get_mode_fouls_per_game(total_fouls_per_game)
    # standard deviation formula using the standard deviation function
    # above and rounded to two decimal places
    standard_dev = (
        round(get_standard_deviation_of_fouls(total_fouls_per_game), 2))

    # mode skew formula
    mode_skew = (mean - mode) / standard_dev

    # returns the mode skew
    return mode_skew


def get_median_skewness_of_fouls(total_fouls_per_game):
    """
    Get the median skewness skewness from the data

    Args:
        total_fouls_per_game (list[int]): list of integers to calculate
        median skewness from

    Returns:
        median_skew: the median skewness
        skewness from the data
    """
    # mean value formula sum of list values passed
    # divided by the length of the list
    mean = sum(total_fouls_per_game) / len(total_fouls_per_game)
    # get the mode of list passed by calling the get mode fouls
    # function declared above
    mode = get_mode_fouls_per_game(total_fouls_per_game)
    # standard deviation formula using the standard deviation function
    # above and rounded to two decimal places
    standard_dev = get_standard_deviation_of_fouls(total_fouls_per_game)

    # median skew formula
    median_skew = (3 * (mean - mode)) / standard_dev

    # returns the median skew
    return median_skew


def get_covariance_between_datasets(home_fouls, away_fouls):
    """
    Gets the covariance between ywo lists of integers from the data

    Args:
        home_fouls (list[int]): list of integers containing home
        fouls per game per season
        away_fouls (list[int]): list of integers containing away
        fouls per game per season

    Returns:
        co_var: the co variance between the two lists of integers
    """
    # gets and declares a mean value for home fouls
    home_mean = sum(home_fouls) / len(home_fouls)
    # gets and declares a mean value for away fouls
    away_mean = sum(away_fouls) / len(away_fouls)
    # initialises an empty list
    totals = []
    # loops through two lists at the same time
    for home, away in zip(home_fouls, away_fouls):
        # appends new values to totals list based on the formula
        # each home value and away value on an iteration of the
        # loop will minus the mean values found above
        totals.append((home - home_mean) * (away - away_mean))
    # declares a new variable equal to the sum of the values in totals list
    total_values = sum(totals)
    # declares co variance to equal the co variance between data sets
    co_var = total_values / (len(home_fouls))
    # returns the co variance
    return co_var


def get_correlation_of_fouls(home_fouls, away_fouls):
    """
    Gets the correlation between two lists of integers from the data

    Args:
        home_fouls (list[int]): list of integers containing home
        fouls per game per season
        away_fouls (list[int]): list of integers containing away
        fouls per game per season

    Returns:
        correlation: the correlation between the two lists.
    """
    # gets and declares a mean value for home fouls
    home_avg = sum(home_fouls) / len(home_fouls)
    # gets and declares a mean value for away fouls
    away_avg = sum(away_fouls) / len(away_fouls)
    # new list initialised
    mean_diff_home = []
    # new list initialised
    mean_diff_away = []
    # loops through two lists at the same time
    for home_foul, away_foul in zip(home_fouls, away_fouls):
        # appends new value to list based on
        # each home_foul iteration minus the
        # home_avg found above
        mean_diff_home.append(home_foul-home_avg)
        # appends new value to list based on
        # each away_foul iteration minus the
        # away_avg found above
        mean_diff_away.append(away_foul-away_avg)
    # new list initialised
    home_sqr_list = []
    # new list initialised
    away_sqr_list = []
    # new list initialised
    diff = []
    # loops through two lists at the same time
    for home_diff, away_diff in zip(mean_diff_home, mean_diff_away):
        # appends new value to list initialised home_sqr_list
        # new value is equal to the home_diff squared on each
        # loop iteration
        home_sqr_list.append(home_diff*home_diff)
        # appends new value to list initialised away_sqr_list
        # new value is equal to the away_diff squared on each
        # loop iteration
        away_sqr_list.append(away_diff*away_diff)
        # appends new value to list initialised diff
        # new value is equal to the home_diff multiply away_diff
        # on each loop iteration
        diff.append(home_diff*away_diff)
    # new variable declared for correlation which equals the formula to
    # find the correlation which is the sum of the diff list divided by
    # the square root of the the sum of the home_sqr_list multiplied by
    # the sum of the away_sqr_list
    correlation = (
        sum(diff) / ((sum(home_sqr_list) * sum(away_sqr_list)) ** 0.5))
    # returns the correlation value
    return correlation
