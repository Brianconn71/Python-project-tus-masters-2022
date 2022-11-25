from calculations import *

def print_statements():
    print(f"The average number of fouls per game for the 2021/22 season was {average_fouls} fouls")
    print(f"The median number of fouls per game over the course of the 21/22 season is: {median_fouls:.1f}")
    print(f"The mode number of fouls per game over the course of the 21/22 season is: {mode_fouls}")
    print(f"The maximum number of fouls in a game over the course of the 21/22 season was: {max_fouls}")
    print(f"The minimum number of fouls in a game over the course of the 21/22 season was: {min_fouls}")
    print(f"The range of fouls in a game over the course of the 21/22 season was: {range_of_fouls}")
    print(f"The interquartile range of fouls in a game over the course of the 21/22 season was: {interquartile_range}")
    print(f"The standard deviation of fouls in a game over the course of the 21/22 season was: {standard_dev:.2f}")
    print(f"The Pearson Mode Skewness of fouls in a game over the course of the 21/22 season was: {pearson_mode:.2f}")
    print(f"The Alternative Pearson Mode Skewness of fouls in a game over the course of the 21/22 season was: {alternative_pearson:.2f}")
    print(f"The correlation between the data is {correlation:.2f}")


if __name__ == "__main__":
    read_data_and_create_lists()
    total_games = len(home_fouls)
    average_fouls = get_average_fouls_per_game(total_games)
    total_fouls_per_game = get_total_fouls_per_game_in_season()
    median_fouls = get_median_fouls_per_game(total_fouls_per_game)
    mode_fouls = get_mode_fouls_per_game(total_fouls_per_game)
    max_fouls = get_maximum_fouls_in_a_game(total_fouls_per_game)
    min_fouls = get_minimum_fouls_in_a_game(total_fouls_per_game)
    range_of_fouls = get_range_of_fouls(max_fouls, min_fouls)
    interquartile_range = get_interquartile_range_of_fouls(total_fouls_per_game)
    standard_dev = get_standard_deviation_of_fouls(total_fouls_per_game,total_games)
    pearson_mode = get_pearson_mode_skewness_of_fouls(total_games, total_fouls_per_game)
    alternative_pearson = get_alternative_pearson_mode_skewness_of_fouls(total_games, total_fouls_per_game)
    co_variance = get_covariance_between_datasets(home_fouls, away_fouls)
    correlation = get_correlation_of_fouls(home_fouls, away_fouls)
    print_statements()