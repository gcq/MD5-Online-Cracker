import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.post("http://md5pass.info/",
                        data={"hash":h,
                              "get_pass":"Get+Pass"}).text
    soup = bs(web)
    for node in soup.find_all("form")[1].next_siblings:
        if node.name == "b":
            return node.text

print(get_plaintext("9cdfb439c7876e703e307864c9167a16"))
