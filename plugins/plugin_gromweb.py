import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.get("http://md5.gromweb.com/?md5={}".format(h)).text
    soup = bs(web)
    return soup.find(id="form_string")["value"]
