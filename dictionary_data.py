from main import *
import pydoc

referees_data = {}

def distinct_sub_categories(ref_data, total_fouls_per_game):
    # referees_data[referees_data]
    for ref , fouls_in_game in zip(ref_data, total_fouls_per_game):
        referees_data[ref] = referees_data.get(ref,0) + fouls_in_game
    print(len(referees_data.keys()))


if __name__ == "__main__":
    read_data_and_create_lists()
    total_fouls_per_game = get_total_fouls_per_game_in_season()
    distinct_sub_categories(referees, total_fouls_per_game)