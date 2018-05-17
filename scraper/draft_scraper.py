import collections
import json

import requests
from bs4 import BeautifulSoup

NBA_URL = 'http://www.basketball-reference.com/draft/NBA_%s.html'
BAA_URL = 'http://www.basketball-reference.com/draft/BAA_%s.html'


def scrape(year):
    return parse(request(year))


def request(year):
    url = NBA_URL if year > 1949 else BAA_URL  # league name changed after 1949
    return requests.get(url % year)


def parse(response):
    draft = collections.OrderedDict()  # need keys ordered for the csv header
    soup = BeautifulSoup(response.text, 'html.parser').find('table', id='stats')

    headings = [
        th['data-stat']
        for th in soup.find('thead').find_all('tr')[1].find_all('th')
    ]

    for tr in soup.find_all('tr'):
        player = collections.OrderedDict()

        cols = tr.find_all('td')
        if len(cols) == 0:
            continue
        if tr.find('th'):
            cols.insert(0, tr.find('th'))
        for index, td in enumerate(cols):
            player[headings[index]] = td.string

        rank_col = 'ranker' if not player['pick_overall'] else 'pick_overall'
        draft[int(player[rank_col])] = player

    return draft


if __name__ == '__main__':
    y = 1996
    d = scrape(y)
    print(json.dumps(d, indent=2))
