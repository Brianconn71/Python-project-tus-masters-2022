from main import *
import pydoc

referees_data = {}

def distinct_sub_categories(ref_data, home_fouls, away_fouls):
    # referees_data[referees_data]
    total = []
    for y, z in zip(home_fouls, away_fouls):
        trt = y + z
        total.append(trt)
    for er , nm in zip(ref_data, total):
        referees_data[er] = referees_data.get(er,0) + nm
    print("osf")
    # test


if __name__ == "__main__":
    read_data_and_create_lists()
    distinct_sub_categories(referees, home_fouls, away_fouls)