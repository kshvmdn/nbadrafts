import collections
import json

import requests
from bs4 import BeautifulSoup

NBA_URL = 'http://www.basketball-reference.com/draft/NBA_%s.html'
BAA_URL = 'http://www.basketball-reference.com/draft/BAA_%s.html'


def scrape(year):
    return parse(request(year))


def request(year):
    url = NBA_URL if year > 1949 else BAA_URL
    return requests.get(url % year)


def parse(response):
    draft = collections.OrderedDict()
    soup = BeautifulSoup(response.text, 'html.parser').find('table', id='stats')

    headings = []
    for th in soup.find('thead').find_all('tr')[1].find_all('th'):
        headings.append(th['data-stat'])

    for tr in soup.find_all('tr'):
        player = collections.OrderedDict()
        if not tr.find('th'):
            for index, td in enumerate(tr.find_all('td')):
                player[headings[index]] = td.string
            if not player['pick_overall']:
                draft[int(player['ranker'])] = player
            else:
                draft[int(player['pick_overall'])] = player
    return draft


if __name__ == '__main__':
    y = 1996
    d = scrape(y)
    print(json.dumps(d, indent=2))
