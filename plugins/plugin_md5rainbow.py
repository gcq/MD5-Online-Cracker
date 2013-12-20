import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.get("http://www.md5rainbow.com/{}".format(h)).text
    soup = bs(web)
    value = soup.find("h1").next_sibling.strip()
    if value:
        return value
    else:
        return None
