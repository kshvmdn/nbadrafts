import collections
import csv
import matplotlib.pyplot as plt
import numpy as np
import pprint

CSV_PATH = 'datasets/%s_nbadraft.csv'


def convert_empty_string(val):
    return 0 if val == '' else val


def plot(players):
    labels = [player[0] for player in players]
    x_data = [player[1] for player in players]
    y_data = [player[2] * 1 + player[4] * 4 + player[3] * 2 for player in players]

    fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'), figsize=(20, 6))
    ax.scatter(
        x_data, 
        y_data, 
        c=np.random.random(size=len(x_data)),
        s=150,
        alpha=0.4,
        cmap=plt.cm.jet)
    ax.grid(color='white', linestyle='solid')
    ax.set_title('NBA Draft rank vs. Score')

    ax.set_xlim([min(x_data)-2, max(x_data)+2])
    ax.set_ylim([min(y_data)-2, max(y_data)+2])
    

    plt.xticks(np.arange(min(x_data)+4, max(x_data)+1, 5.0))
    plt.yticks(np.arange(min(y_data), max(y_data), 5.0))

    plt.xlabel('Draft Rank')
    plt.ylabel('Score (ppg + 2 · apg + 4 · rpg)')

    plt.show()


def populate_player_list(year):
    players = []
    with open(CSV_PATH % str(year)) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = [ row['player'], int(row['ranker']) ]
            player.append( float(convert_empty_string(row['pts_per_g'])) )
            player.append( float(convert_empty_string(row['trb_per_g'])) )
            player.append( float(convert_empty_string(row['ast_per_g'])) )
            players.append(player)
    return players

if __name__ == '__main__':
    plot(populate_player_list(2015))
