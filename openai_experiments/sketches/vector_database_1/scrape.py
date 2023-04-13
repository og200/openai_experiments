"""
Scrape a given set of web pages to extract text for embedding and indexing.

Note that this tool is designed to be tweaked to extract relevant text and avoid navigation, footers, etc.
"""

from pathlib import Path
import time

import bs4
import requests
import sqlitedict

import openai_experiments

data_path = Path(openai_experiments.__file__).parent / 'data'

cache = sqlitedict.SqliteDict(data_path / 'vector_database_1_scrape.sqlite', autocommit=True)


urls = [
    'https://parknationalbank.com/personal/personal-bank/health-savings-accounts/',
]

def fetch_with_cache(url):
    if url in cache:
        return cache[url]
    else:
        rc = requests.get(url)
        cache[url] = rc.content
        return rc.content

def text(s):
    out = ''
    for j in i.find_all(text=True):
        out += j + '\n'
    return


def scrape():
    for url in urls:
        print(url)
        html = fetch_with_cache(url)
        s = bs4.BeautifulSoup(html)
        title = s.find_all('h1').find
        out = ''
        for i in s.find_all('p'):
        print(out)


if __name__ == '__main__':
    scrape()