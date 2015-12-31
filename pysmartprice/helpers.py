import requests


def scrape(url):
    resp = requests.get(url)
    return resp.text
