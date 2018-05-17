import csv
import os
from datetime import date

from scraper.draft_scraper import scrape

OUTDIR = 'datasets'
OUTFILE = '%s/%s_nbadraft.csv'

if __name__ == '__main__':
    if not os.path.exists(OUTDIR):
        os.makedirs(OUTDIR)

    for year in range(1947, date.today().year):
        draft = scrape(year)
        header = [key for key in draft[1].keys()]
        with open(OUTFILE % (OUTDIR, year), 'w', newline='') as outfile:
            dw = csv.DictWriter(outfile, header)
            dw.writeheader()
            dw.writerows([row for index, row in draft.items()])
        print('Data processed for %s.' % year)
