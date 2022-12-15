from dictionary_visualisations import (
    pie_chart_from_data, box_plots_from_dict, bar_chart_from_data)
from calculations import read_data_and_create_lists
import pytest


def test_pie_chart_from_data():
    """
    tests that a pie chart will correctly plot from the dictionary passed
    """
    # calls the function with a dictionary argument
    pie_chart_from_data({"B connolly": 23.5, "A man": 14.2})
    # asserts true if function plots
    assert True


def test_box_plots_from_dict():
    """
    tests that a box plot will correctly plot from the dictionary passed
    """
    # calls the function with a dictionary argument
    box_plots_from_dict({"B connolly": 23.5, "A man": 14.2})
    # asserts true if function plots
    assert True


def test_bar_chart_from_data():
    """
    tests that a bar chart will correctly plot from the dictionary passed
    """
    # calls the function with a dictionary argument
    bar_chart_from_data({"B connolly": 23.5, "A man": 14.2})
    # asserts true if function plots
    assert True


if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data
    # from csv and split into lists
    read_data_and_create_lists()
    pytest.main(["test_dictionary_visualisations.py", "-vv"])
