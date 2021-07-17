import requests
from bs4 import BeautifulSoup


def hltv_get(pUser:str,pCategory:str) -> dict:
    response = requests.get("")
    hltv_base = response.content
    hltv_content = BeautifulSoup(hltv_base,"html.parser")
    print('HLTV CALLED')
    return f'<h1>HLTV LOADED</h1>'