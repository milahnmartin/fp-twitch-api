import requests
import keys
from bs4 import BeautifulSoup


def faceit(pUser:str,pCategory:str) -> None:
    h = {"Authorization":"Bearer " + keys.API_KEY}
    response = requests.get(f"https://open.faceit.com/data/v4/players?nickname={pUser}&game=CSGO",headers=h)
    print(response.text)
    # return f'<h1>FACEIT LOADED</h1>'



faceit(None,None)