# importing functions from all other files
from calculations import *
from dictionary_calculations import *
from visualisations import *
from dictionary_visualisations import *

# function to print all statements to the console
def print_statements():
    """
    This function prints all the requirements for the project to the console
    """    
    # printing average fouls to console
    print(f"The average number of fouls per game for the 2021/22 season was {average_fouls} fouls")
    # printing median fouls to console
    print(f"The median number of fouls per game over the course of the 21/22 season is: {median_fouls:.1f}")
    # printing the mode number of fouls to console
    print(f"The mode number of fouls per game over the course of the 21/22 season is: {mode_fouls}")
    # printing the max fouls in a game to console
    print(f"The maximum number of fouls in a game over the course of the 21/22 season was: {max_fouls}")
    # printing the minimum fouls in a game to console
    print(f"The minimum number of fouls in a game over the course of the 21/22 season was: {min_fouls}")
    # printing the range of fouls in a game to console
    print(f"The range of fouls in a game over the course of the 21/22 season was: {range_of_fouls}")
    # printing the interquartile range of fouls in a game to console
    print(f"The interquartile range of fouls in a game over the course of the 21/22 season was: {interquartile_range}")
    # printing the standard deviation fouls in a game to console
    print(f"The standard deviation of fouls in a game over the course of the 21/22 season was: {standard_dev:.2f}")
    # printing the pearson mode skew of fould in a game to console
    print(f"The Pearson Mode Skewness of fouls in a game over the course of the 21/22 season was: {pearson_mode:.2f}")
    # printing the alternative pearson mode skew of fouls in a game to console
    print(f"The Alternative Pearson Mode Skewness of fouls in a game over the course of the 21/22 season was: {alternative_pearson:.2f}")
    # printing the correlation of home fouls to away fouls in 21/22 season
    print(f"The correlation between the data is {correlation:.2f}")
    # printing the distinct number of regeree sub categories
    print(f"The distinct number of referees is: {sub_categories}")
    # printing the referee who gave the most fouls in 21/22
    print(f"The referee who gave the most fouls in the 2021/22 season was: {ref_with_most_fouls}")
    # printing the referee who gave the least fouls in 21/22
    print(f"The referee who gave the least fouls in the 2021/22 season was: {ref_with_least_fouls}")
    # printing the referee who gave the highest average oof fouls per game in which they officiated in 21/22
    print(highest_avg_fouls_per_game)
    # printing the referee who gave the lowest average oof fouls per game in which they officiated in 21/22
    print(lowest_avg_fouls_per_game)


if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data from csv and split into lists
    read_data_and_create_lists()
    # uses the length of the home_fouls list (always has at least one value) to calculate total games
    total_games = len(home_fouls)
    # gets the average fouls per game in season from get_average_fouls_per_game function in calculations.py
    average_fouls = get_average_fouls_per_game(total_games)
    # gets the total fouls per game in season from get_total_fouls_per_game_in_season function in calculations.py
    total_fouls_per_game = get_total_fouls_per_game_in_season()
    # gets the median fouls per game in season from get_median_fouls_per_game function in calculations.py
    median_fouls = get_median_fouls_per_game(total_fouls_per_game)
    # gets the mode number of fouls per game in season from get_mode_fouls_per_game function in calculations.py
    mode_fouls = get_mode_fouls_per_game(total_fouls_per_game)
    # gets the max number of fouls per game in season from get_maximum_fouls_in_a_game function in calculations.py
    max_fouls = get_maximum_fouls_in_a_game(total_fouls_per_game)
    # gets the meinimum number of fouls per game in season from get_minimum_fouls_in_a_game function in calculations.py
    min_fouls = get_minimum_fouls_in_a_game(total_fouls_per_game)
    # gets the range of fouls per game in season from get_range_of_fouls function in calculations.py
    range_of_fouls = get_range_of_fouls(max_fouls, min_fouls)
    # gets the interquartile range of fouls per game in season from get_interquartile_range_of_fouls function in calculations.py
    interquartile_range = get_interquartile_range_of_fouls(total_fouls_per_game)
    # gets the standard deviation of fouls per game in season from get_standard_deviation_of_fouls function in calculations.py
    standard_dev = get_standard_deviation_of_fouls(total_fouls_per_game,total_games)
    # gets the pearson mode skew of fouls per game in season from get_pearson_mode_skewness_of_fouls function in calculations.py
    pearson_mode = get_pearson_mode_skewness_of_fouls(total_games, total_fouls_per_game)
    # gets the alternative pearson mode skew of fouls per game in season from get_alternative_pearson_mode_skewness_of_fouls function in calculations.py
    alternative_pearson = get_alternative_pearson_mode_skewness_of_fouls(total_games, total_fouls_per_game)
    # gets the co Variance of fouls between home and away teams in season from get_covariance_between_datasets function in calculations.py
    co_variance = get_covariance_between_datasets(home_fouls, away_fouls)
    # gets the correlation of fouls between home and away teams in season from get_correlation_of_fouls function in calculations.py
    correlation = get_correlation_of_fouls(home_fouls, away_fouls)
    # calling the histogram_from_data from visualisations.py to create a histogram from home and away fouls and place diagram in charts folder
    histogram_from_data(home_fouls, away_fouls)
    # calling the box_plots_from_data from visualisations.py to create a box plot from home and away fouls and place diagram in charts folder
    box_plots_from_data(home_fouls, away_fouls)
    # calling the scatter_plot_from_data from visualisations.py to create a scatter plot from home and away fouls and place diagram in charts folder
    scatter_plot_from_data(home_fouls, away_fouls)
    # adds unique sub categories with count of occurances (games reffered) to a dictionary in dictionary_calculations.py using get_dict_of_refs_and_occurances_in_data function
    referees_count_of_games_data = get_dict_of_refs_and_occurances_in_data(referees)
    # adds unique referees and total count of fouls for 21/22 season to a dictionary in dictionary_calculations.py using get_total_refs_data function
    referees_total_fouls_data = get_total_refs_data(referees, total_fouls_per_game)
    # gets the unique number of referrees sub categories and returns for use in print statement from dictionary_calculations.py using function distinct_sub_categories
    sub_categories = distinct_sub_categories(referees_total_fouls_data)
    # gets the referee with most fouls given and returns for use in print statement from dictionary_calculations.py using function ref_with_most_fouls_given
    ref_with_most_fouls = ref_with_most_fouls_given(referees_total_fouls_data)
    # gets the referee with least fouls given and returns for use in print statement from dictionary_calculations.py using function ref_with_least_fouls_given
    ref_with_least_fouls = ref_with_least_fouls_given(referees_total_fouls_data)
    # creates a dictionary with referees and the average fouls given per game by that referee from dictionary_calculations.py using function dict_from_average_fouls_per_game
    average_fouls_per_game_dict = dict_from_average_fouls_per_game(referees_total_fouls_data, num_of_games_reffed)
    # gets the referee with highest average of fouls given and returns for use in print statement from dictionary_calculations.py using function ref_with_highest_average_of_fouls_given_per_game
    highest_avg_fouls_per_game = ref_with_highest_average_of_fouls_given_per_game(average_fouls_per_game_dict)
    # gets the referee with the lowest average of fouls given and returns for use in print statement from dictionary_calculations.py using function ref_with_lowest_average_of_fouls_given_per_game
    lowest_avg_fouls_per_game = ref_with_lowest_average_of_fouls_given_per_game(average_fouls_per_game_dict)
    # calling the print_statements function above to print statements to the console
    print_statements()