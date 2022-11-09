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

def get_median_fouls_per_game():
    total_fouls_per_game_in_season = []
    for home,away in zip(home_fouls, away_fouls):
        fouls = home + away
        total_fouls_per_game_in_season.append(fouls)
    sorted_list_fouls_per_game = sorted(total_fouls_per_game_in_season)
    middle_value = int(len(sorted_list_fouls_per_game) / 2)
    if len(sorted_list_fouls_per_game) % 2 == 1:
        median_value = sorted_list_fouls_per_game[middle_value]
    else:
        median_value = ((sorted_list_fouls_per_game[middle_value - 1] + sorted_list_fouls_per_game[middle_value]) / 2)
    print(f"Median number of fouls per game over the course of the 21/22 season is: {median_value:.1f}")


def get_mode_fouls_per_game():
    pass

def get_maximum_fouls_in_a_game():
    pass

def get_minimum_fouls_in_a_game():
    pass


# matplotlib stuff
# plt.plot(x,y)
# plt.show()


if __name__ == "__main__":
    read_data_and_create_lists()
    get_number_of_games_in_season()
    get_median_fouls_per_game()