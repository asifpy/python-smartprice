import requests


def scrape(url, **kwargs):
    resp = requests.get(url, params=kwargs)
    return resp.text


def scrape_helper(args):
    return scrape(args[0], **args[1])
