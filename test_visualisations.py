from visualisations import *
from calculations import *
import pytest

def test_histogram_from_data():
    histogram_from_data([1,2,3,4,5,6,7], [1,2,3,4,5,6,7])
    assert True

def test_scatter_plot_from_data():
    scatter_plot_from_data([1,2,3,4,5,6,7], [1,2,3,4,5,6,7])
    assert True

def test_box_plots_from_data():
    box_plots_from_data([1,2,3,4,5,6,7], [1,2,3,4,5,6,7])
    assert True

if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to read data from csv and split into lists
    read_data_and_create_lists()
    pytest.main(["test_visualisations.py", "-vv"])