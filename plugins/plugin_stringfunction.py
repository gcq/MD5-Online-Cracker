import requests
from bs4 import BeautifulSoup as bs


def get_plaintext(h):
    web = requests.post("http://www.stringfunction.com/md5-decrypter.html",
                        data={"string_md5":h,
                              "string":"",
                              "submit":"Decrypt",
                              "result":""}).text
    soup = bs(web)
    value = soup.find(id="textarea_md5_decrypter").text
    if value:
        return value
    else:
        return None
