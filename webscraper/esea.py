import requests
from bs4 import BeautifulSoup

def esea_get(pUser:str,pCategory:str) -> dict:
    response = requests.get("")
    esea_base = response.content
    esea_content = BeautifulSoup(esea_base,"html.parser")
    print('ESEA LOADED')
    return f'<h1>ESEA LOADED</h1>'