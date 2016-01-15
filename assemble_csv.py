import sys, csv
from datetime import date

from scraper import scrape

CSV_FILE = 'datasets/%s_nbadraft.csv'

for year in range(1947, date.today().year):
    draft = scrape(year)
    header = [key for key in draft[1].keys()]
    with open(CSV_FILE % year, 'w', newline='') as outfile:
        dw = csv.DictWriter(outfile, header)
        dw.writeheader()
        for i, row in draft.items():
            dw.writerow(row)
