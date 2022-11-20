from main import *
import matplotlib.pyplot as plt

def histogram_from_data(home_fouls, away_fouls):
    # creates the figure and axis object
    fig, ax = plt.subplots(1,2, figsize=(15,10))
    
    fig.suptitle("Visualisations of fouls throughout 21/22 season")
    
    #sets title
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
    
    #show the histograms
    plt.show()
    # save the figures as a png
    fig.savefig("histograms.png")

def box_plots_from_data():
    pass

def scatter_plot_from_data():
    pass

if __name__ == "__main__":
    read_data_and_create_lists()
    histogram_from_data(home_fouls, away_fouls)