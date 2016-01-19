import collections
import csv
import matplotlib.pyplot as plt
import pprint

CSV_PATH = 'datasets/%s_nbadraft.csv'


def plot(points, pick):
    n, bins, patches = plt.hist(karma, 100, facecolor='green', alpha=0.75)

    plt.xlabel('Karma')
    plt.ylabel('Post count')
    plt.gca().set_yscale('log')
    plt.grid(True)

    plt.show()


players = []

def populate_players(year):
    player = {}
    with open(CSV_PATH % str(year)) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # score scale (stat, worth)
            # pt, 1
            # ast, 2
            # rbd, 4
            player_details = [row['player'], row['ranker'], row['pts_per_g'], row['trb_per_g'], row['ast_per_g']]
            players.append(player_details)


populate_player_dict(2015)
pprint.pprint(players)
