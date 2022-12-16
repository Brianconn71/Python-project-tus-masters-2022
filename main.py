# Student ID: A00204916
"""
This file is used as the brain of the project,
it runs the entire program
"""
# importing functions from all other files
from calculations import (
    read_data_and_create_lists, get_average_fouls_per_game,
    get_total_fouls_per_game_in_season, get_median_fouls_per_game,
    get_mode_fouls_per_game, get_maximum_fouls_in_a_game,
    get_minimum_fouls_in_a_game, get_range_of_fouls,
    get_interquartile_range_of_fouls, get_standard_deviation_of_fouls,
    get_pearson_mode_skewness_of_fouls,
    get_alternative_pearson_mode_skewness_of_fouls,
    get_covariance_between_datasets, get_correlation_of_fouls,
    get_total_fouls_per_list,
    home_fouls, away_fouls, referees)
from dictionary_calculations import (
    get_dict_of_refs_and_occurances_in_data, get_total_refs_data,
    distinct_sub_categories, ref_with_most_fouls_given,
    ref_with_least_fouls_given, dict_from_average_fouls_per_game,
    ref_with_highest_average_of_fouls_given_per_game,
    ref_with_lowest_average_of_fouls_given_per_game,
    num_of_games_reffed)
from visualisations import (
    histogram_from_data, box_plots_from_data,
    scatter_plot_from_data)
from dictionary_visualisations import (
    pie_chart_from_data, bar_chart_from_data,
    box_plots_from_dict)


# function to print all statements to the console
def print_statements():
    """
    This function prints all the requirements for the project to the console
    """
    # user menu loop starting point
    while True:
        # user prompted to choose to examine home, away or both sets of fouls
        # or to quit the program
        user_input = input(("Press [H] to examine home fouls"
                            ", Press [A] to examine away fouls"
                            ", Press [B] to examine both"
                            ", or press [Q] to quit"))
        if user_input.lower().startswith("q"):
            break
        elif user_input.lower().startswith("h"):
            total_home_fouls = get_total_fouls_per_list(home_fouls)
            print(f"The total number of Home fouls for the 2021/22 "
                  f"season was {total_home_fouls} fouls")
            median_fouls = get_median_fouls_per_game(home_fouls)
            print(f"The total number of Home fouls for the 2021/22 "
                  f"season was {median_fouls} fouls")
            # gets the mode number of fouls per game in season from
            # get_mode_fouls_per_game function in calculations.py
            mode_fouls = get_mode_fouls_per_game(home_fouls)
            # gets the max number of fouls per game in season from
            # get_maximum_fouls_in_a_game function in calculations.py
            max_fouls = get_maximum_fouls_in_a_game(home_fouls)
            # gets the meinimum number of fouls per game in season from
            # get_minimum_fouls_in_a_game function in calculations.py
            min_fouls = get_minimum_fouls_in_a_game(home_fouls)
            # gets the range of fouls per game in season from
            # get_range_of_fouls function in calculations.py
            range_of_fouls = get_range_of_fouls(max_fouls, min_fouls)
            # gets the interquartile range of fouls per game in season from
            # get_interquartile_range_of_fouls function in calculations.py
            interquartile_range = get_interquartile_range_of_fouls(
                home_fouls)
            # gets the standard deviation of fouls per game in season from
            # get_standard_deviation_of_fouls function in calculations.py
            standard_dev = get_standard_deviation_of_fouls(home_fouls)
            # gets the pearson mode skew of fouls per game in season from
            # get_pearson_mode_skewness_of_fouls function in calculations.py
            pearson_mode = get_pearson_mode_skewness_of_fouls(home_fouls)
            # gets the alternative pearson mode skew of fouls per game in season from
            # get_alternative_pearson_mode_skewness_of_fouls function in calculations
            alternative_pearson = get_alternative_pearson_mode_skewness_of_fouls(
                home_fouls)
        elif user_input.lower().startswith("a"):
            total_away_fouls = get_total_fouls_per_list(away_fouls)
            print(f"The total number of Home fouls for the 2021/22 "
                  f"season was {total_away_fouls} fouls")
            median_fouls = get_median_fouls_per_game(away_fouls)
            print(f"The total number of Home fouls for the 2021/22 "
                  f"season was {median_fouls} fouls")
            # gets the mode number of fouls per game in season from
            # get_mode_fouls_per_game function in calculations.py
            mode_fouls = get_mode_fouls_per_game(away_fouls)
            # gets the max number of fouls per game in season from
            # get_maximum_fouls_in_a_game function in calculations.py
            max_fouls = get_maximum_fouls_in_a_game(away_fouls)
            # gets the meinimum number of fouls per game in season from
            # get_minimum_fouls_in_a_game function in calculations.py
            min_fouls = get_minimum_fouls_in_a_game(away_fouls)
            # gets the range of fouls per game in season from
            # get_range_of_fouls function in calculations.py
            range_of_fouls = get_range_of_fouls(max_fouls, min_fouls)
            # gets the interquartile range of fouls per game in season from
            # get_interquartile_range_of_fouls function in calculations.py
            interquartile_range = get_interquartile_range_of_fouls(
                away_fouls)
            # gets the standard deviation of fouls per game in season from
            # get_standard_deviation_of_fouls function in calculations.py
            standard_dev = get_standard_deviation_of_fouls(away_fouls)
            # gets the pearson mode skew of fouls per game in season from
            # get_pearson_mode_skewness_of_fouls function in calculations.py
            pearson_mode = get_pearson_mode_skewness_of_fouls(away_fouls)
            # gets the alternative pearson mode skew of fouls per game in season from
            # get_alternative_pearson_mode_skewness_of_fouls function in calculations
            alternative_pearson = get_alternative_pearson_mode_skewness_of_fouls(
                away_fouls)
        elif user_input.lower().startswith("b"):
            try:
                # printing average fouls to console
                print(
                    f"The average number of fouls per game for the 2021/22 "
                    f"season was {average_fouls} fouls")
            except NameError:
                print("average fouls is not defined.")
            try:
                # printing median fouls to console
                print(
                    f"The median number of fouls per game over the course of "
                    f"the 21/22 season is: {median_fouls:.1f}")
            except NameError:
                print("median fouls is not defined.")
            try:
                # printing the mode number of fouls to console
                print(
                    f"The mode number of fouls per game over the course of "
                    f"the 21/22 season is: {mode_fouls}")
            except NameError:
                print("mode_fouls is not defined.")
            try:
                # printing the max fouls in a game to console
                print(
                    f"The maximum number of fouls in a game over the course "
                    f"of the 21/22 season was: {max_fouls}")
            except NameError:
                print("max_fouls is not defined.")
            try:
                # printing the minimum fouls in a game to console
                print(
                    f"The minimum number of fouls in a game over the course "
                    f"of the 21/22 season was: {min_fouls}")
            except NameError:
                print("min_fouls is not defined.")
            try:
                # printing the range of fouls in a game to console
                print(
                    f"The range of fouls in a game over the course of the "
                    f"21/22 season was: {range_of_fouls}")
            except NameError:
                print("range_of_fouls is not defined.")
            try:
                # printing the interquartile range of fouls in a game
                # to console
                print(
                    f"The interquartile range of fouls in a game over the "
                    f"course of the 21/22 season was: {interquartile_range}")
            except NameError:
                print("interquartile_range is not defined.")
            try:
                # printing the standard deviation fouls in a game to console
                print(
                    f"The standard deviation of fouls in a game over the "
                    f"course of the 21/22 season was: {standard_dev:.2f}")
            except NameError:
                print("standard_dev is not defined.")
            try:
                # printing the pearson mode skew of fould in a game to console
                print(
                    f"The Pearson Mode Skewness of fouls in a game over the "
                    f"course of the 21/22 season was: {pearson_mode:.2f}")
            except NameError:
                print("pearson_mode is not defined.")
            try:
                # printing the alternative pearson mode skew of fouls in a game
                # to console
                print(
                    f"The Alternative Pearson Mode Skewness of fouls in a game"
                    f" over the course of the 21/22 season was: "
                    f"{alternative_pearson:.2f}")
            except NameError:
                print("alternative_pearson is not defined.")
            try:
                # printing the correlation of home fouls to away fouls in
                # 21/22 season
                print(f"The correlation between the data is {correlation:.2f}")
            except NameError:
                print("correlation is not defined.")
            try:
                # printing the distinct number of regeree sub categories
                print(f"The distinct number of referees is: {sub_categories}")
            except NameError:
                print("sub_categories is not defined.")
            try:
                # printing the referee who gave the most fouls in 21/22
                print(ref_with_most_fouls)
            except NameError:
                print("ref_with_most_fouls is not defined.")
            try:
                # printing the referee who gave the least fouls in 21/22
                print(ref_with_least_fouls)
            except NameError:
                print("ref_with_least_fouls is not defined.")
            try:
                # printing the referee who gave the highest average of fouls
                # per game in which they officiated in 21/22
                print(highest_avg_fouls_per_game)
            except NameError:
                print("highest_avg_fouls_per_game is not defined.")
            try:
                # printing the referee who gave the lowest average of fouls
                # per game in which they officiated in 21/22
                print(lowest_avg_fouls_per_game)
            except NameError:
                print("lowest_avg_fouls_per_game is not defined.")
        else:
            print(f"{user_input[0]} is incorrect, please pick again.")


if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data
    # from csv and split into lists
    read_data_and_create_lists()
    # uses the length of the home_fouls list (always has at least one value)
    # to calculate total games
    total_games = len(home_fouls)
    # gets the average fouls per game in season from get_average_fouls_per_game
    # function in calculations.py
    average_fouls = get_average_fouls_per_game(total_games)
    # gets the total fouls per game in season from
    # get_total_fouls_per_game_in_season function in calculations.py
    total_fouls_per_game = get_total_fouls_per_game_in_season(
        home_fouls, away_fouls)
    # gets the median fouls per game in season from get_median_fouls_per_game
    # function in calculations.py
    median_fouls = get_median_fouls_per_game(total_fouls_per_game)
    # gets the mode number of fouls per game in season from
    # get_mode_fouls_per_game function in calculations.py
    mode_fouls = get_mode_fouls_per_game(total_fouls_per_game)
    # gets the max number of fouls per game in season from
    # get_maximum_fouls_in_a_game function in calculations.py
    max_fouls = get_maximum_fouls_in_a_game(total_fouls_per_game)
    # gets the meinimum number of fouls per game in season from
    # get_minimum_fouls_in_a_game function in calculations.py
    min_fouls = get_minimum_fouls_in_a_game(total_fouls_per_game)
    # gets the range of fouls per game in season from
    # get_range_of_fouls function in calculations.py
    range_of_fouls = get_range_of_fouls(max_fouls, min_fouls)
    # gets the interquartile range of fouls per game in season from
    # get_interquartile_range_of_fouls function in calculations.py
    interquartile_range = get_interquartile_range_of_fouls(
        total_fouls_per_game)
    # gets the standard deviation of fouls per game in season from
    # get_standard_deviation_of_fouls function in calculations.py
    standard_dev = get_standard_deviation_of_fouls(total_fouls_per_game)
    # gets the pearson mode skew of fouls per game in season from
    # get_pearson_mode_skewness_of_fouls function in calculations.py
    pearson_mode = get_pearson_mode_skewness_of_fouls(total_fouls_per_game)
    # gets the alternative pearson mode skew of fouls per game in season from
    # get_alternative_pearson_mode_skewness_of_fouls function in calculations
    alternative_pearson = get_alternative_pearson_mode_skewness_of_fouls(
        total_fouls_per_game)
    # gets the co Variance of fouls between home and away teams in season from
    # get_covariance_between_datasets function in calculations.py
    co_variance = get_covariance_between_datasets(home_fouls, away_fouls)
    # gets the correlation of fouls between home and away teams in season from
    # get_correlation_of_fouls function in calculations.py
    correlation = get_correlation_of_fouls(home_fouls, away_fouls)
    # calling the histogram_from_data from visualisations.py to
    # create a histogram from home and away fouls and
    # place diagram in charts folder
    histogram_from_data(home_fouls, away_fouls)
    # calling the box_plots_from_data from visualisations.py to
    # create a box plot from home and away fouls and
    # place diagram in charts folder
    box_plots_from_data(home_fouls, away_fouls)
    # calling the scatter_plot_from_data from visualisations.py to
    # create a scatter plot from home and away fouls and
    # place diagram in charts folder
    scatter_plot_from_data(home_fouls, away_fouls)
    # adds unique sub categories with count of occurances (games reffered) to
    # a dictionary in dictionary_calculations.py using
    # get_dict_of_refs_and_occurances_in_data function
    referees_count_of_games_data = get_dict_of_refs_and_occurances_in_data(
        referees)
    # adds unique referees and total count of fouls for 21/22 season to
    # a dictionary in dictionary_calculations.py using get_total_refs_data
    # function
    referees_total_fouls_data = get_total_refs_data(
        referees, total_fouls_per_game)
    # gets the unique number of referrees sub categories and returns for use
    # in print statement from dictionary_calculations.py using
    # function distinct_sub_categories
    sub_categories = distinct_sub_categories(referees_total_fouls_data)
    # gets the referee with most fouls given and returns for use in print
    # statement from dictionary_calculations.py using
    # function ref_with_most_fouls_given
    ref_with_most_fouls = ref_with_most_fouls_given(referees_total_fouls_data)
    # gets the referee with least fouls given and returns for use in print
    # statement from dictionary_calculations.py using
    # function ref_with_least_fouls_given
    ref_with_least_fouls = ref_with_least_fouls_given(
        referees_total_fouls_data)
    # creates a dictionary with referees and the average fouls given per game
    # by that referee from dictionary_calculations.py
    # using function dict_from_average_fouls_per_game
    average_fouls_per_game_dict = dict_from_average_fouls_per_game(
        referees_total_fouls_data, num_of_games_reffed)
    # gets the referee with highest average of fouls given and returns for use
    # in print statement from dictionary_calculations.py using
    # function ref_with_highest_average_of_fouls_given_per_game
    highest_avg_fouls_per_game = (
        ref_with_highest_average_of_fouls_given_per_game(
            average_fouls_per_game_dict))
    # gets the referee with the lowest average of fouls given and returns for
    # use in print statement from dictionary_calculations.py
    # using function ref_with_lowest_average_of_fouls_given_per_game
    lowest_avg_fouls_per_game = (
        ref_with_lowest_average_of_fouls_given_per_game(
            average_fouls_per_game_dict))
    # calling the pie_chart_from_data from dictionary_visualisations.py to
    # create a pie chart from total referees data dictionary and
    # place diagram in charts folder
    pie_chart_from_data(referees_total_fouls_data)
    # calling the bar_chart_from_data from dictionary_visualisations.py to
    # create a horizontal bar chart from average referees data dictionary
    # and place diagram in charts folder
    bar_chart_from_data(average_fouls_per_game_dict)
    # calling the box_plots_from_dict from dictionary_visualisations.py to
    # create a box plot from average referees data dictionary and
    # place diagram in charts folder
    box_plots_from_dict(average_fouls_per_game_dict)
    # calling the print_statements function above to
    # print statements to the console
    print_statements()
