import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.post("http://md5online.net/",
                        data={"pass":h,
                              "option":"hash2text"}).text
    soup = bs(web)
    try:
        return soup.find_all("center")[2].find_all("b")[1].text
    except IndexError:
        return None
