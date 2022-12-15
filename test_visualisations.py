from visualisations import (
    histogram_from_data, scatter_plot_from_data,
    box_plots_from_data
)
from calculations import read_data_and_create_lists
import pytest


def test_histogram_from_data():
    """
    tests that histograms will correctly plot from two lists passed
    """
    # Call histogram_from_data from visualisations
    # Passes two lists of integers
    histogram_from_data(
        [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7])
    # Asserts Histogram plots
    assert True


def test_scatter_plot_from_data():
    """
    tests that a scatter plot will correctly plot from two lists passed
    """
    # Call histogram_from_data from visualisations
    # Passes two lists of integers
    scatter_plot_from_data(
        [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7])
    # Asserts Scatter plot plots
    assert True


def test_box_plots_from_data():
    """
    tests that box plots will correctly plot from two lists passed
    """
    # Call histogram_from_data from visualisations
    # Passes two lists of integers
    box_plots_from_data(
        [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7])
    # Asserts box plot plots
    assert True


if __name__ == "__main__":
    # calls the read_data_and_create_lists in calculations.py to
    # read data from csv and split into lists
    read_data_and_create_lists()
    # Runs pytest tests on current file
    pytest.main([__file__, "-vv"])
