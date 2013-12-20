import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.get("http://www.md5-hash.com/md5-hashing-decrypt/{}".format(h)).text
    soup = bs(web)
    try:
        return soup.find("strong", class_="result").text
    except AttributeError:
        return None
