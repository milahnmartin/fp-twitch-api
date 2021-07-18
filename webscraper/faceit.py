import requests
from bs4 import BeautifulSoup


def faceit(pUser:str,pCategory:str) -> dict:
    response = requests.get("")
    faceit_base = response.content
    faceit_content = BeautifulSoup(faceit_base,"lxml")
    print('HLTV CALLED')
    return f'<h1>HLTV LOADED</h1>'