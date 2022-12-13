import matplotlib.pyplot as plt

def pie_chart_from_data(average_fouls_dict):
    # fig and ax declarations
    fig, ax = plt.subplots(figsize=(15,10))

    # setting title
    ax.set_title("Pie chart showing average number of fouls per referee as a percentage of total fouls over the 2021/22 season")

    # creating the pie charts
    ax.pie(average_fouls_dict.values(), labels=average_fouls_dict.keys(), autopct="%.2f%%")

    # show the figure
    plt.show()

    # save the figure
    fig.savefig("charts/pieChart.png")

def bar_chart_from_data(average_fouls_dict):

    #fig and ax
    fig, ax = plt.subplots(figsize=(15,10))

    # set title
    ax.set_title("Average fouls per game by referee")

    # set avix labels
    ax.set_ylabel("Referees")
    ax.set_xlabel("Fouls")

    # create bar cahrt
    ax.barh(list(average_fouls_dict.keys()), average_fouls_dict.values())

    #display average values per referee
    for index, value in enumerate(average_fouls_dict.values()):
        ax.text(value, index, str(value))
    
    # show plot
    plt.show()

    # save figure
    fig.savefig("charts/barChart.png")

def box_plots_from_dict(average_fouls_dict):
    # creating figure and axis of objecdts
    fig, ax = plt.subplots(figsize=(15,10))
    
    #set labels on y axes
    ax.set_ylabel("Average fouls")
    
    # set title
    ax.set_title("Average number of fouls given by each referee per game")
    
    # box plot
    ax.boxplot(average_fouls_dict.values())
    
    # display
    plt.show()
    
    #save the fig
    fig.savefig('charts/boxplots_from_dictionary.png', bbox_inches='tight')
