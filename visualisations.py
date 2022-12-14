import matplotlib.pyplot as plt


def histogram_from_data(home_fouls, away_fouls):
    """
    Plots two histograms from lists of integers pssed

    Args:
        home_fouls (list[int]): list of integers
        away_fouls (list[int]): list of integers
    """
    # creates the figure and axis object
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))

    fig.suptitle("Visualisations of fouls throughout 21/22 season")

    # sets title
    ax[0].set_title("Home Fouls")

    ax[0].set_xlabel("Fouls")
    ax[0].set_ylabel("Frequency")

    x_bins = range(1, int(max(home_fouls)))

    ax[0].set_xticks(x_bins)
    ax[0].hist(home_fouls, x_bins, ec="black")

    ax[1].set_title("Away Fouls")

    ax[1].set_xlabel("Fouls")
    ax[1].set_ylabel("Frequency")

    y_bins = range(1, int(max(away_fouls)))

    ax[1].set_xticks(y_bins)
    ax[1].hist(away_fouls, y_bins, ec="black")

    # show the histograms
    plt.show()
    # save the figures as a png
    fig.savefig("charts/histograms.png")


def box_plots_from_data(home_fouls, away_fouls):
    """
    Plots two box plots from list of integers passed

    Args:
        home_fouls (list[int]): list of integers
        away_fouls (list[int]): list of integers
    """
    # creating figure and axis of objecdts
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))

    # set labels on y axes
    ax[0].set_ylabel("Number of Home Fouls")

    # set title
    ax[0].set_title("Home fouls 21/22")

    # box plot
    ax[0].boxplot(home_fouls)

    # set labels on y axes
    ax[1].set_ylabel("Number of Away Fouls")

    # set title
    ax[1].set_title("away fouls 21/22")

    # box plot
    ax[1].boxplot(away_fouls)

    # display
    plt.show()

    # save the fig
    fig.savefig('charts/boxplots.png', bbox_inches='tight')


def scatter_plot_from_data(home_fouls, away_fouls):
    """
    Plots a scater plot from two lists passed

    Args:
        home_fouls (list[int]): list of integers
        away_fouls (list[int]): list of integers
    """
    # create figure and axis objects
    fig, ax = plt.subplots(figsize=(10, 8))

    # setting the labels on axes
    ax.set_xlabel("Home Fouls")
    ax.set_ylabel("Away fouls")

    # set the title
    ax.set_title("Fouls 21/22")

    # Do the scatter plot
    ax.scatter(home_fouls, away_fouls, marker=".")

    # display the scatter plot
    plt.show()

    # save to image
    fig.savefig('charts/Scatterplot.png', bbox_inches='tight')
