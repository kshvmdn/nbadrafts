import requests
import pprint
import collections
from bs4 import BeautifulSoup

BASE_URL = 'http://www.basketball-reference.com/draft/NBA_%s.html'


def scrape(year):
    return parse(request(year))


def request(year):
    return requests.get(BASE_URL % year)


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
            draft[int(player['pick_overall'])] = player
    return draft


if __name__ == '__main__':
    y = 2015
    scrape(y)
