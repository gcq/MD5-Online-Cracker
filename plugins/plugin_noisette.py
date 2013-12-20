import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.get("http://md5.noisette.ch/md5.php?hash={}".format(h)).text
    soup = bs(web, "xml")
    if soup.find("error"):
        return None
    else:
        s = soup.find("string")
        if s:
            return s.text
