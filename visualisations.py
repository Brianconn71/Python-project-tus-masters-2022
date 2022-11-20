from main import *
import matplotlib.pyplot as plt

def histogram_from_data(home_fouls, away_fouls):
    fig, ax = plt.subplots(1,2, figsize=(15,10))
    
    fig.suptitle("Visualisations of fouls throughout 21/22 season")
    
    ax[0].set_title("Home Fouls")
    
    ax[0].set_xlabel("Fouls")
    ax[0].set_ylabel("Frequency")
    
    bins = range(0, int(max(home_fouls)) + 2)
    
    ax[0].set_xticks(bins)
    ax[0].hist(home_fouls, bins, ec="black")
    
    plt.show()
    # save the figure
    fig.savefig("exercise_1.png")

def box_plots_from_data():
    pass

def scatter_plot_from_data():
    pass

if __name__ == "__main__":
    read_data_and_create_lists()
    histogram_from_data(home_fouls, away_fouls)