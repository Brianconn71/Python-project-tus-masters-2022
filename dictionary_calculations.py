import pydoc

total_referees_data = {}
num_of_games_reffed = {}
ref_with_avg_value = {}


def get_dict_of_refs_and_occurances_in_data(referees):
    """
    gets the list of referees, counts its occuraancws in the list and
    adds the values to a dictionary

    Args:
        referees (list[str]): list of strings

    Returns:
        num_of_games_reffed (Dict): dictionary of unique referees and
        how often they have reffed games
    """
    # find unique values in list
    unique_values = set(referees)
    # loop through unique values
    for value in unique_values:
        # add unique value to the dictionary
        # along with the count of occurances in
        # referees list
        num_of_games_reffed[value] = referees.count(value)
    # return the dictionary with number of occurances
    return num_of_games_reffed


def get_total_refs_data(ref_data, total_fouls_per_game):
    """
    takes in a list of referees and a list of integers with total fouls and
    returns a dictionary with referees as keys and the total fouls they
    gave over the season as the values

    Args:
        ref_data (list[str]): list of strings
        total_fouls_per_game (list[int]): list of integers

    Returns:
        total_referees_data (dict): dictionary of unique referees
        total fouls given over season
    """
    # loop through two lists of values
    for ref, fouls_in_game in zip(ref_data, total_fouls_per_game):
        # add the ref in ref_data list to a dictionary
        # as a key and adds the refs total fouls
        # as a value
        total_referees_data[ref] = (
            total_referees_data.get(ref, 0) + fouls_in_game)
    # returns a new dictionary with each ref and total fouls given by each ref
    return total_referees_data


def distinct_sub_categories(total_referees_data):
    """
    This fucntion will take in a dictionary of referees data and gets the
    len of the dict.keys() to return distict number of referees

    Args:
        total_referees_data (dict): dictionary of referees and
        total fouls given

    Returns:
        number_of_referees (int): distinct number of referees
    """
    # get number of refs by getting length of total refs data keys
    number_of_referees = len(total_referees_data.keys())
    # prints dictinct number to console
    print(f"The distinct number of referees is: {number_of_referees}")
    # returns the distinct number of referees
    return number_of_referees


def dict_from_average_fouls_per_game(referees_data, num_of_games_reffed):
    """
    takes in two dictionaries representing refereed data and returns a new dict
    with the referee and average fouls given by each referee

    Args:
        referees_data (dict): dictionary of referees and total fouls given
        num_of_games_reffed (dict): dictionary of referees and
        number of games referred

    Returns:
        ref_with_avg_value (dict): a new dictionary with referees and their
        average fouls given over the season
    """
    # loops through referees data dictionary
    for ref, fouls in referees_data.items():
        # checks if the referee is in the number of games reffed
        # dictionary keys
        if ref in num_of_games_reffed.keys():
            # calculates each refs average value of fouls given
            average_value = round(fouls / num_of_games_reffed[ref], 2)
            # adds this value with the referee as key to a new dictinoary
            ref_with_avg_value[ref] = average_value
    # calls the ref_with_highest_average_of_fouls_given_per_game function with
    # the new dictionary of referees with average fouls
    ref_with_highest_average_of_fouls_given_per_game(ref_with_avg_value)
    # calls the ref_with_lowest_average_of_fouls_given_per_game function with
    # the new dictionary of referees with average fouls
    ref_with_lowest_average_of_fouls_given_per_game(ref_with_avg_value)
    # returns the new dictionary ref_with_avg_value
    return ref_with_avg_value


def ref_with_most_fouls_given(referees_data):
    """
    Gets the ref  who gave most fouls in 21/22 by taking the max value from a
    dictionary displaying ref data and total fouls given by each

    Args:
        referees_data (dict): dictionary of referees and total fouls given

    Returns:
        ref_with_most_fouls (str): string value of ref who gave most fouls
    """
    # find the referee key in the refrees data dictionary who gave most fouls
    ref_with_most_fouls = max(referees_data, key=referees_data.get)
    # finds the corresponding value of the max fouls given from the dictionary
    num_of_fouls_given = max(referees_data.values())
    # string to print to console with name of ref who gave most fouls
    # and the value
    ref_with_most_fouls = (f"The referee who gave the most fouls in the"
                           f" 2021/22 season was: {ref_with_most_fouls} "
                           f"with a total fouls given of {num_of_fouls_given}")
    # returns formatted string
    return ref_with_most_fouls


def ref_with_least_fouls_given(referees_data):
    """
    Gets the ref  who gave least fouls in 21/22 by taking the min value from a
    dictionary displaying ref data and total fouls given by each

    Args:
        referees_data (dict): dictionary of referees and total fouls given

    Returns:
        ref_with_least_fouls (str): string value of ref who gave least fouls
    """
    # find the referee key in the refrees data dictionary who gave least fouls
    ref_with_least_fouls = min(referees_data, key=referees_data.get)
    # finds the corresponding value of the min fouls given from the dictionary
    num_of_fouls_given = min(referees_data.values())
    # string to print to console with name of ref who gave least fouls
    # and the value
    ref_with_least_fouls = (f"The referee who gave the least fouls in the "
                            f"2021/22 season was: {ref_with_least_fouls} with "
                            f"a total fouls given of {num_of_fouls_given}")
    # returns formatted string
    return ref_with_least_fouls


def ref_with_highest_average_of_fouls_given_per_game(ref_with_avg_value):
    """
    Gets the ref  who gave highest average of fouls in 21/22 by taking the
    value from a dictionary displaying ref data and average given by each

    Args:
        ref_with_avg_value (dict): dictionary of referees and average
        fouls given per game

    Returns:
        highest_avg_value (str): string value of ref had the highest average
        of fouls per game
    """
    # find the referee key in the refrees average data dictionary who gave
    # highest average of fouls
    ref_with_highest_average = max(
        ref_with_avg_value, key=ref_with_avg_value.get)
    # find the average value in the refrees average data dictionary who gave
    # highest average of fouls
    highest_average = ref_with_avg_value[ref_with_highest_average]
    # string to print to console with name of ref who gave highest average
    # of fouls and the value
    highest_avg_value = (f"The referee who had the highest average of fouls "
                         f"given per game in the 2021/22 season was: "
                         f"{ref_with_highest_average} with an average fouls "
                         f"per game of {highest_average}")
    # returns formatted string
    return highest_avg_value


def ref_with_lowest_average_of_fouls_given_per_game(ref_with_avg_value):
    """
    Gets the ref  who gave lowest average of fouls in 21/22 by taking the
    value from a dictionary displaying ref data and average given by each

    Args:
        ref_with_avg_value (dict): dictionary of referees and
        average fouls per game

    Returns:
        lowest_average_value (str): string value of ref had the
        lowest average of fouls per game
    """
    # find the referee key in the refrees average data dictionary who gave
    # lowest average of fouls
    ref_with_lowest_average = min(
        ref_with_avg_value, key=ref_with_avg_value.get)
    # find the average value in the refrees average data dictionary who gave
    # lowest average of fouls
    lowest_average = ref_with_avg_value[ref_with_lowest_average]
    # string to print to console with name of ref who gave lowest average
    # of fouls and the value
    lowest_average_value = (
        f"The referee who had the lowest average of fouls given per game "
        f"in the 2021/22 season was: {ref_with_lowest_average} with an average"
        f" fouls per game of {lowest_average} ")
    # returns formatted string
    return lowest_average_value
