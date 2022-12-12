from visualisations import *
from calculations import *
from dictionary_calculations import *
import pytest

def test_pie_chart_from_data():
    pie_chart_from_data({"B connolly": 23.5, "A man": 14.2})
    assert True

def test_box_plots():
    box_plots({"B connolly": 23.5, "A man": 14.2})
    assert True

def test_bar_chart_from_data():
    bar_chart_from_data({"B connolly": 23.5, "A man": 14.2})
    assert True

if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data from csv and split into lists
    read_data_and_create_lists()
    pytest.main(["test_dictionary_visualisations.py", "-vv"])