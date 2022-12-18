# Student ID: A00204916
"""
This file is used as the brain of the project,
it runs the entire program
"""
# importing functions from all other files
from calculations import (
    read_data_and_create_lists,
    get_total_fouls_per_game_in_season, get_median_fouls_per_game,
    get_mode_fouls_per_game, get_maximum_fouls_in_a_game,
    get_minimum_fouls_in_a_game, get_range_of_fouls,
    get_interquartile_range_of_fouls, get_standard_deviation_of_fouls,
    get_mode_skewness_of_fouls, get_median_skewness_of_fouls,
    get_correlation_of_fouls, get_total_fouls_per_list,
    get_mean_fouls_per_game, home_fouls, away_fouls, referees)
from dictionary_calculations import (
    get_dict_of_refs_and_occurances_in_data, get_total_refs_data,
    distinct_sub_categories, ref_with_most_fouls_given,
    ref_with_least_fouls_given, dict_from_average_fouls_per_game,
    ref_with_highest_average_of_fouls_given_per_game,
    ref_with_lowest_average_of_fouls_given_per_game)
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
                            ", or press [Q] to quit"))
        # if user input is q then loop breaks
        if user_input.lower().startswith("q"):
            # break the loop
            break
        # if user input is h then analyse home fouls data
        elif user_input.lower().startswith("h"):
            # gets the total number of fouls in season from
            # get_total_fouls_per_list function in calculations.py
            total_home_fouls = get_total_fouls_per_list(home_fouls)
            # printing total number of fouls to console
            print(f"The total number of Home fouls for the 2021/22 "
                  f"season was {total_home_fouls} fouls")
            # asks the users for input to get mean value
            get_mean = input("Get the mean? [Y}es or [Q]uit?")
            # if input is y then get the mean value
            if get_mean.lower().startswith("y"):
                # calls get_mean_fouls_per_game function
                # n calculations to get mean from home fouls list
                mean_fouls = get_mean_fouls_per_game(home_fouls)
                # printing average fouls to console
                print(
                    f"The average number of fouls per game for the 2021/22 "
                    f"season was {mean_fouls:.2f} fouls")
            # if user input is q then loop breaks
            elif get_mean.lower().startswith("q"):
                break
            # asks the users for input to get median value
            get_median = input("Get the median? [Y}es or [Q]uit?")
            # if input is y then get the median value
            if get_median.lower().startswith("y"):
                # calls get_median_fouls_per_game function
                # n calculations to get median from home fouls list
                median_fouls = get_median_fouls_per_game(home_fouls)
                # printing median fouls to console
                print(
                    f"The median number of fouls per game over the course of "
                    f"the 21/22 season is: {median_fouls:.1f}")
            # if user input is q then loop breaks
            elif get_median.lower().startswith("q"):
                break
            # asks the users for input to get mode value
            get_mode = input("Get the mode? [Y}es or [Q]uit?")
            # if input is y then get the mode value
            if get_mode.lower().startswith("y"):
                # gets the mode number of fouls per game in season from
                # get_mode_fouls_per_game function in calculations.py
                mode_fouls = get_mode_fouls_per_game(home_fouls)
                # printing the mode number of fouls to console
                print(
                    f"The mode number of fouls per game over the course of "
                    f"the 21/22 season is: {mode_fouls}")
            # if user input is q then loop breaks
            elif get_mode.lower().startswith("q"):
                break
            # asks the users for input to get max value
            get_max = input("Get the max value? [Y}es or [Q]uit?")
            # if input is y then get the max value
            if get_max.lower().startswith("y"):
                # gets the max number of fouls per game in season from
                # get_maximum_fouls_in_a_game function in calculations.py
                max_fouls = get_maximum_fouls_in_a_game(home_fouls)
                # printing the max fouls in a game to console
                print(
                    f"The maximum number of fouls in a game over the course "
                    f"of the 21/22 season was: {max_fouls}")
            # if user input is q then loop breaks
            elif get_max.lower().startswith("q"):
                break
            # asks the users for input to get min value
            get_min = input("Get the minimum value? [Y}es or [Q]uit?")
            # if input is y then get the min value
            if get_min.lower().startswith("y"):
                # gets the meinimum number of fouls per game in season from
                # get_minimum_fouls_in_a_game function in calculations.py
                min_fouls = get_minimum_fouls_in_a_game(home_fouls)
                # printing the minimum fouls in a game to console
                print(
                    f"The minimum number of fouls in a game over the course "
                    f"of the 21/22 season was: {min_fouls}")
            # if user input is q then loop breaks
            elif get_min.lower().startswith("q"):
                break
            # asks the users for input to get range value
            get_range = input("Get the range? [Y}es or [Q]uit?")
            # if input is y then get the range value
            if get_range.lower().startswith("y"):
                # gets the range of fouls per game in season from
                # get_range_of_fouls function in calculations.py
                range_of_fouls = get_range_of_fouls(max_fouls, min_fouls)
                # printing the range of fouls in a game to console
                print(
                    f"The range of fouls in a game over the course of the "
                    f"21/22 season was: {range_of_fouls}")
            # if user input is q then loop breaks
            elif get_range.lower().startswith("q"):
                break
            # asks the users for input to get interquartile value
            get_iqr = input("Get the interquartile range? [Y}es or [Q]uit?")
            # if input is y then get the interquartile value
            if get_iqr.lower().startswith("y"):
                # gets the interquartile range of fouls per game in season from
                # get_interquartile_range_of_fouls function in calculations.py
                interquartile_range = get_interquartile_range_of_fouls(
                    home_fouls)
                # printing the interquartile range of fouls in a game
                # to console
                print(
                    f"The interquartile range of fouls in a game over the "
                    f"course of the 21/22 season was: {interquartile_range}")
            # if user input is q then loop breaks
            elif get_iqr.lower().startswith("q"):
                break
            # asks the users for input to get standard deviation value
            get_standard_dev = input("Get the standard deviation? [Y}es or"
                                     " [Q]uit?")
            # if input is y then get the standard deviation value
            if get_standard_dev.lower().startswith("y"):
                # gets the standard deviation of fouls per game in season from
                # get_standard_deviation_of_fouls function in calculations.py
                standard_dev = get_standard_deviation_of_fouls(home_fouls)
                # printing the standard deviation fouls in a game to console
                print(
                    f"The standard deviation of fouls in a game over the "
                    f"course of the 21/22 season was: {standard_dev:.2f}")
            # if user input is q then loop breaks
            elif get_standard_dev.lower().startswith("q"):
                break
            # asks the users for input to get mode skewness value
            get_mode_skew = input("Get the mode skew? [Y}es or [Q]uit?")
            # if input is y then get the mode skewness value
            if get_mode_skew.lower().startswith("y"):
                # gets the mode skew of fouls per game in season from
                # get_mode_skewness_of_fouls function in calculations.py
                mode_skew = get_mode_skewness_of_fouls(home_fouls)
                # printing the mode skew of fould in a game to console
                print(
                    f"The mode skewness of fouls in a game over the "
                    f"course of the 21/22 season was: {mode_skew:.2f}")
            # if user input is q then loop breaks
            elif get_mode_skew.lower().startswith("q"):
                break
            # asks the users for input to get median skewness value
            get_median_skew = input("Get the median skew? [Y}es or [Q]uit?")
            # if input is y then get the median skewness value
            if get_median_skew.lower().startswith("y"):
                # gets the median skew of fouls per game in season from
                # get_alternative_mode_skewness_of_fouls function
                # in calculations
                median_skew = get_median_skewness_of_fouls(
                    home_fouls)
                # printing the median skew of fouls in a game
                # to console
                print(
                    f"The median skewness of fouls in a game"
                    f" over the course of the 21/22 season was: "
                    f"{median_skew:.2f}")
            # if user input is q then loop breaks
            elif get_median_skew.lower().startswith("q"):
                break
        # if user input is a then analyse away fouls data
        elif user_input.lower().startswith("a"):
            # gets the total number of fouls in season from
            # get_total_fouls_per_list function in calculations.py
            total_away_fouls = get_total_fouls_per_list(away_fouls)
            # printing total number of fouls to console
            print(f"The total number of away fouls for the 2021/22 "
                  f"season was {total_away_fouls} fouls")
            # asks the users for input to get mean value
            get_mean = input("Get the mean? [Y}es or [Q]uit?")
            # if input is y then get the mean value
            if get_mean.lower().startswith("y"):
                # calls get_mean_fouls_per_game function
                # n calculations to get mean from away fouls list
                mean_fouls = get_mean_fouls_per_game(away_fouls)
                # printing average fouls to console
                print(
                    f"The average number of fouls per game for the 2021/22 "
                    f"season was {mean_fouls:.2f} fouls")
            # if user input is q then loop breaks
            elif get_mean.lower().startswith("q"):
                break
            # asks the users for input to get median value
            get_median = input("Get the median? [Y}es or [Q]uit?")
            # if input is y then get the median value
            if get_median.lower().startswith("y"):
                # calls get_median_fouls_per_game function
                # n calculations to get median from away fouls list
                median_fouls = get_median_fouls_per_game(away_fouls)
                # printing median fouls to console
                print(
                    f"The median number of fouls per game over the course of "
                    f"the 21/22 season is: {median_fouls:.1f}")
            # if user input is q then loop breaks
            elif get_median.lower().startswith("q"):
                break
            # asks the users for input to get mode value
            get_mode = input("Get the mode? [Y}es or [Q]uit?")
            # if input is y then get the mode value
            if get_mode.lower().startswith("y"):
                # gets the mode number of fouls per game in season from
                # get_mode_fouls_per_game function in calculations.py
                mode_fouls = get_mode_fouls_per_game(away_fouls)
                # printing the mode number of fouls to console
                print(
                    f"The mode number of fouls per game over the course of "
                    f"the 21/22 season is: {mode_fouls}")
            # if user input is q then loop breaks
            elif get_mode.lower().startswith("q"):
                break
            # asks the users for input to get max value
            get_max = input("Get the max value? [Y}es or [Q]uit?")
            # if input is y then get the max value
            if get_max.lower().startswith("y"):
                # gets the max number of fouls per game in season from
                # get_maximum_fouls_in_a_game function in calculations.py
                max_fouls = get_maximum_fouls_in_a_game(away_fouls)
                # printing the max fouls in a game to console
                print(
                    f"The maximum number of fouls in a game over the course "
                    f"of the 21/22 season was: {max_fouls}")
            # if user input is q then loop breaks
            elif get_max.lower().startswith("q"):
                break
            # asks the users for input to get min value
            get_min = input("Get the minimum value? [Y}es or [Q]uit?")
            # if input is y then get the min value
            if get_min.lower().startswith("y"):
                # gets the meinimum number of fouls per game in season from
                # get_minimum_fouls_in_a_game function in calculations.py
                min_fouls = get_minimum_fouls_in_a_game(away_fouls)
                # printing the minimum fouls in a game to console
                print(
                    f"The minimum number of fouls in a game over the course "
                    f"of the 21/22 season was: {min_fouls}")
            # if user input is q then loop breaks
            elif get_min.lower().startswith("q"):
                break
            # asks the users for input to get range value
            get_range = input("Get the range? [Y}es or [Q]uit?")
            # if input is y then get the range value
            if get_range.lower().startswith("y"):
                # gets the range of fouls per game in season from
                # get_range_of_fouls function in calculations.py
                range_of_fouls = get_range_of_fouls(max_fouls, min_fouls)
                # printing the range of fouls in a game to console
                print(
                    f"The range of fouls in a game over the course of the "
                    f"21/22 season was: {range_of_fouls}")
            # if user input is q then loop breaks
            elif get_range.lower().startswith("q"):
                break
            # asks the users for input to get interquartile value
            get_iqr = input("Get the interquartile range? [Y}es or [Q]uit?")
            # if input is y then get the interquartile value
            if get_iqr.lower().startswith("y"):
                # gets the interquartile range of fouls per game in season from
                # get_interquartile_range_of_fouls function in calculations.py
                interquartile_range = get_interquartile_range_of_fouls(
                    away_fouls)
                # printing the interquartile range of fouls in a game
                # to console
                print(
                    f"The interquartile range of fouls in a game over the "
                    f"course of the 21/22 season was: {interquartile_range}")
            # if user input is q then loop breaks
            elif get_iqr.lower().startswith("q"):
                break
            # asks the users for input to get standard deviation value
            get_standard_dev = input("Get the standard deviation? [Y}es or"
                                     " [Q]uit?")
            # if input is y then get the standard deviation value
            if get_standard_dev.lower().startswith("y"):
                # gets the standard deviation of fouls per game in season from
                # get_standard_deviation_of_fouls function in calculations.py
                standard_dev = get_standard_deviation_of_fouls(away_fouls)
                # printing the standard deviation fouls in a game to console
                print(
                    f"The standard deviation of fouls in a game over the "
                    f"course of the 21/22 season was: {standard_dev:.2f}")
            # if user input is q then loop breaks
            elif get_standard_dev.lower().startswith("q"):
                break
            # asks the users for input to get mode skewness value
            get_mode_skew = input("Get the mode skew?  [Y}es or [Q]uit?")
            # if input is y then get the mode skewness value
            if get_mode_skew.lower().startswith("y"):
                # gets the mode skew of fouls per game in season from
                # get_mode_skewness_of_fouls function in calculations.py
                mode_skew = get_mode_skewness_of_fouls(away_fouls)
                # printing the pearson mode skew of fould in a game to console
                print(
                    f"The mode skewness of fouls in a game over the "
                    f"course of the 21/22 season was: {mode_skew:.2f}")
            # if user input is q then loop breaks
            elif get_mode_skew.lower().startswith("q"):
                break
            # asks the users for input to get median skewness value
            get_median_skew = input("Get the median skew? [Y}es or [Q]uit?")
            # if input is y then get the median skewness value
            if get_median_skew.lower().startswith("y"):
                # gets the median skew of fouls per game in season from
                # get_median_skewness_of_fouls function in calculations
                median_skew = get_median_skewness_of_fouls(
                    away_fouls)
                # printing the median skew of fouls in a game
                # to console
                print(
                    f"The median skewness of fouls in a game"
                    f" over the course of the 21/22 season was: "
                    f"{median_skew:.2f}")
            # if user input is q then loop breaks
            elif get_median_skew.lower().startswith("q"):
                break
        # if user selects anything else then message displays an error.
        else:
            print(f"{user_input[0]} is incorrect, please pick again.")


def correlation_and_dictionary():
    while True:
        # user prompted to choose to examine Correlation and Dictionary data
        # or to quit the program
        user_input = input(("Press [Y] to examine Correlation and Dictionary"
                            " data, or press [Q] to quit"))
        # if user input is q then loop breaks
        if user_input.lower().startswith("q"):
            # break the loop
            break
        # if user input is y then analsyse data
        elif user_input.lower().startswith("y"):
            # asks the users for input to get correlation value
            get_correlation = input("Get the correlation between home"
                                    " and away fouls? [Y}es or [Q]uit?")
            # if input is y then get the correlation value
            if get_correlation.lower().startswith("y"):
                # gets the correlation of fouls between home and away teams
                # in season from
                # get_correlation_of_fouls function in calculations.py
                correlation = get_correlation_of_fouls(home_fouls, away_fouls)
                # printing the correlation of home fouls to away fouls in
                # 21/22 season
                print(f"The correlation between the data is {correlation:.2f}")
            # if user input is q then loop breaks
            elif get_correlation.lower().startswith("q"):
                break
            # asks the users for input to get a histogram chart
            get_histogram = input("Get the histogram showing home"
                                  " and away fouls? [Y}es or [Q]uit?")
            # if input is y then get a histogram chart
            if get_histogram.lower().startswith("y"):
                # calling the histogram_from_data from visualisations.py to
                # create a histogram from home and away fouls and
                # place diagram in charts folder
                histogram_from_data(home_fouls, away_fouls)
            # if user input is q then loop breaks
            elif get_histogram.lower().startswith("q"):
                break
            # asks the users for input to get a box plot chart
            get_box_plots = input("Get the boxplots showing home"
                                  " and away fouls? [Y}es or [Q]uit?")
            # if input is y then get a box plot chart
            if get_box_plots.lower().startswith("y"):
                # calling the box_plots_from_data from visualisations.py to
                # create a box plot from home and away fouls and
                # place diagram in charts folder
                box_plots_from_data(home_fouls, away_fouls)
            # if user input is q then loop breaks
            elif get_box_plots.lower().startswith("q"):
                break
            # asks the users for input to get a scatter plot chart
            get_scatter_plot = input("Get the scatter plot showing home"
                                     " and away fouls? [Y}es or [Q]uit?")
            # if input is y then get a scatter plot chart
            if get_scatter_plot.lower().startswith("y"):
                # calling the scatter_plot_from_data from visualisations.py to
                # create a scatter plot from home and away fouls and
                # place diagram in charts folder
                scatter_plot_from_data(home_fouls, away_fouls)
            # if user input is q then loop breaks
            elif get_scatter_plot.lower().startswith("q"):
                break
            # asks the users for input to get categrical data
            get_dictionary_data = input("Get the categorical data "
                                        "based on referees? [Y}es or [Q]uit?")
            # if input is y then get categorical data
            if get_dictionary_data.lower().startswith("y"):
                # gets the total fouls per game in season from
                # get_total_fouls_per_game_in_season function in calculations
                total_fouls_per_game = get_total_fouls_per_game_in_season(
                    home_fouls, away_fouls)
                # adds unique referees and total count of fouls for 21/22
                # season to a dictionary in dictionary_calculations.py using
                # get_total_refs_data function
                referees_total_fouls_data = get_total_refs_data(
                    referees, total_fouls_per_game)
                # adds unique sub categories with count of occurances
                # (games reffered) to a dictionary in
                # dictionary_calculations.py using
                # get_dict_of_refs_and_occurances_in_data function
                referees_count_of_games_data = (
                    get_dict_of_refs_and_occurances_in_data(
                        referees))
                # creates a dictionary with referees and the average fouls
                # given per game by that referee
                # from dictionary_calculations.py
                # using function dict_from_average_fouls_per_game
                average_fouls_per_game_dict = dict_from_average_fouls_per_game(
                    referees_total_fouls_data, referees_count_of_games_data)
            # if user input is q then loop breaks
            elif get_dictionary_data.lower().startswith("q"):
                break
            # asks the users for input to get distinct sub categories
            get_sub_categories = input("Get the total sub categories "
                                       "based on referees dictionary? [Y}es "
                                       "or [Q]uit?")
            # if input is y then get cdistinct sub categories
            if get_sub_categories.lower().startswith("y"):
                # gets the unique number of referrees sub categories and
                # returns for use in print statement from
                # dictionary_calculations.py using function
                # distinct_sub_categories
                sub_categories = distinct_sub_categories(
                        referees_total_fouls_data)
                # printing the distinct number of regeree sub categories
                print(f"The distinct number of referees is: {sub_categories}")
            # if user input is q then loop breaks
            elif get_sub_categories.lower().startswith("q"):
                break
            # asks the users for input to get the ref who gave the most fouls
            get_most_fouls = input("Get the referee who "
                                   "gave the most fouls? [Y}es or [Q]uit?")
            # if input is y then get the ref qho gave the most fouls
            if get_most_fouls.lower().startswith("y"):
                # gets the referee with most fouls given and returns for use in
                # print statement from dictionary_calculations.py using
                # function ref_with_most_fouls_given
                ref_with_most_fouls = ref_with_most_fouls_given(
                    referees_total_fouls_data)
                # printing the referee who gave the most fouls in 21/22
                print(ref_with_most_fouls)
            # if user input is q then loop breaks
            elif get_most_fouls.lower().startswith("q"):
                break
            # asks the users for input to get the ref who gave the least fouls
            get_least_fouls = input("Get the referee who"
                                    " gave the least fouls? [Y}es or [Q]uit?")
            # if input is y then get the ref qho gave the least fouls
            if get_least_fouls.lower().startswith("y"):
                # gets the referee with least fouls given and returns for use
                # in print statement from dictionary_calculations.py using
                # function ref_with_least_fouls_given
                ref_with_least_fouls = ref_with_least_fouls_given(
                    referees_total_fouls_data)
                # printing the referee who gave the least fouls in 21/22
                print(ref_with_least_fouls)
            # if user input is q then loop breaks
            elif get_least_fouls.lower().startswith("q"):
                break
            # asks the users for input to get the ref who gave the highest
            # averagefouls
            get_highest_avg = input("Get the referee who"
                                    " gave the highest average of fouls? [Y}es"
                                    " or [Q]uit?")
            # if input is y then get the ref qho gave the highest average
            # fouls
            if get_highest_avg.lower().startswith("y"):
                # gets the referee with highest average of fouls given and
                # returns for use in print statement from
                # dictionary_calculations.py using
                # function ref_with_highest_average_of_fouls_given_per_game
                highest_avg_fouls_per_game = (
                    ref_with_highest_average_of_fouls_given_per_game(
                        average_fouls_per_game_dict))
                # printing the referee who gave the highest average of fouls
                # per game in which they officiated in 21/22
                print(highest_avg_fouls_per_game)
            # if user input is q then loop breaks
            elif get_highest_avg.lower().startswith("q"):
                break
            # asks the users for input to get the ref who gave the lowest
            # average fouls
            get_lowest_avg = input("Get the referee who"
                                   " gave the lowest average of fouls? [Y}es "
                                   "or [Q]uit?")
            # if input is y then get the ref qho gave the lowest average
            # fouls
            if get_lowest_avg.lower().startswith("y"):
                # gets the referee with the lowest average of fouls given and
                # returns for use in print statement from
                # dictionary_calculations using function
                # ref_with_lowest_average_of_fouls_given_per_game
                lowest_avg_fouls_per_game = (
                    ref_with_lowest_average_of_fouls_given_per_game(
                        average_fouls_per_game_dict))
                # printing the referee who gave the lowest average of fouls
                # per game in which they officiated in 21/22
                print(lowest_avg_fouls_per_game)
            # if user input is q then loop breaks
            elif get_lowest_avg.lower().startswith("q"):
                break
            # asks the users for input to get pie chart from dict
            get_pie_chart = input("Get a pie chart"
                                  " showing total fouls given by each ref?"
                                  " [Y}es or [Q]uit?")
            # if input is y then get the pie chart
            if get_pie_chart.lower().startswith("y"):
                # calling the pie_chart_from_data from
                # dictionary_visualisations.py to create a pie chart from
                # total referees data dictionary and
                # place diagram in charts folder
                pie_chart_from_data(referees_total_fouls_data)
            # if user input is q then loop breaks
            elif get_pie_chart.lower().startswith("q"):
                break
            # asks the users for input to get bar chart from dict
            get_bar_chart = input("Get a bar chart "
                                  " showing average fouls given by each ref?"
                                  " [Y}es or [Q]uit?")
            # if input is y then get the bar chart
            if get_bar_chart.lower().startswith("y"):
                # calling the bar_chart_from_data from
                # dictionary_visualisations.py to create a horizontal
                # bar chart from average referees data
                # dictionary and place diagram in charts folder
                bar_chart_from_data(average_fouls_per_game_dict)
            # if user input is q then loop breaks
            elif get_bar_chart.lower().startswith("q"):
                break
            # asks the users for input to get box plot chart from dict
            get_box_plot_from_dict = input("Get a box plot showing average "
                                           "fouls given by each ref? [Y}es or"
                                           " [Q]uit?")
            # if input is y then get the box plot chart
            if get_box_plot_from_dict.lower().startswith("y"):
                # calling the box_plots_from_dict from
                # dictionary_visualisations.py to create a box plot
                # from average referees data dictionary and
                # place diagram in charts folder
                box_plots_from_dict(average_fouls_per_game_dict)
            # if user input is q then loop breaks
            elif get_box_plot_from_dict.lower().startswith("q"):
                break
        # if user selects anything else then message displays an error.
        else:
            print(f"{user_input[0]} is incorrect, please pick again.")


if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data
    # from csv and split into lists
    read_data_and_create_lists()
    # calling the print_statements function above to
    # print statements to the console
    print_statements()
    # calling the correlation_and_dictionary function above to
    # get user input on wheteher or not they wish to
    # get the analysis of correclation and dictionary data
    correlation_and_dictionary()
