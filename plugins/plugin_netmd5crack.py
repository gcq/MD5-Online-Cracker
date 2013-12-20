import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.get("http://netmd5crack.com/cgi-bin/Crack.py?InputHash={}".format(h)).text
    soup = bs(web)
    value = soup.find_all("tr")[1].find_all("td")[1].text
    if value != "Sorry, we don't have that hash in our database.":
        return value
    else:
        return None
