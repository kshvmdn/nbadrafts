import sys, csv
from datetime import date

from scraper import scrape

CSV_FILE = 'datasets/%s-DRAFT.csv'

for year in range(2014, date.today().year):
    draft = scrape(year)
    with open(CSV_FILE % year, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dict(draft[1]).keys())
        writer.writeheader()
        for i, row in draft.items():
            writer.writerow(row)
