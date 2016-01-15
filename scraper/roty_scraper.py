import collections
import json

import requests
from bs4 import BeautifulSoup

import pprint

URL = 'http://www.nba.com/history/nba-rookie-of-the-year-award-winners/'


def scrape():
    return parse(request())


def request():
    return requests.get(URL)


def parse(response):
    soup = BeautifulSoup(response, 'html.parser')
    roty = {}
    for tr in soup.find(class_='cnnTMcontent').find_all('tr')[1:]:
        roty[tr.find_all('td')[0].text.strip()] = tr.find_all('td')[1].string.strip()
    pprint.pprint(roty)

if __name__ == '__main__':
    file = open('roty.html')
    parse(file)
    file.close()
