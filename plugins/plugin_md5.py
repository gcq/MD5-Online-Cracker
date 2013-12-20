import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.post("http://www.md5.net/cracker.php",
                        data={"hash":h}).text
    soup = bs(web)
    value = soup.find(id="hash")["value"]
    if value != "Entry not found.":
        return value
    else:
        return None
