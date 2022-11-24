import matplotlib.pyplot as plt

def pie_chart_from_data(new_dict):
    # fig and ax declarations
    fig, ax = plt.subplots(figsize=(15,10))

    # setting title
    ax.set_title("Pie Chart showing Total number of fouls per referee over the 2021/22 season")

    # creating the pie charts
    ax.pie(new_dict.values(), labels=new_dict.keys(), autopct="%.f%%", rotatelabels=True)

    # show the figure
    plt.show()

    # save the figure
    fig.savefig("charts/pieChart.png")

def bar_chart_from_data(data_dict):

    #fig and ax
    fig, ax = plt.subplots(figsize=(15,10))

    # set title
    ax.set_title("Average fouls per game by referee")

    # set avix labels
    ax.set_ylabel("Referees")
    ax.set_xlabel("Average fouls")

    # create bar cahrt
    ax.barh(list(data_dict.keys()), data_dict.values())

    #display average values per referee
    for index, value in enumerate(data_dict.values()):
        ax.text(value, index, str(value))
    
    # show plot
    plt.show()

    # save figure
    fig.savefig("charts/barChart.png")

def box_plots(data_dict):
    # creating figure and axis of objecdts
    fig, ax = plt.subplots(figsize=(15,10))
    
    #set labels on y axes
    ax.set_ylabel("Number of Home Fouls")
    
    # set title
    ax.set_title("Home fouls 21/22")
    
    # box plot
    ax.boxplot(home_fouls)
    
    #set labels on y axes
    ax.set_ylabel("Number of Away Fouls")
    
    # set title
    ax.set_title("away fouls 21/22")
    
    # box plot
    ax.boxplot(away_fouls)
    
    # display
    plt.show()
    
    #save the fig
    fig.savefig('charts/boxplots.png', bbox_inches='tight')

if __name__ == "__main__":
    pass