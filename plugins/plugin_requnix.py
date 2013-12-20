import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.get("http://requnix.tk/md5/api/txt.php?md5={}".format(h)).text
    if web:
        return web
    else:
        return None
