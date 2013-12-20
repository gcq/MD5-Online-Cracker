import requests


def get_plaintext(h):
    json = requests.get("https://api.leakdb.net/?j={}".format(h)).json()
    try:
        return json["hashes"][0]["plaintext"]
    except KeyError:
        return None
