from bs4 import BeautifulSoup
import urllib.request

def faceit_get(pUser:str,pCategory:str):
    url = "https://www.faceit.com/en/players/Fadey-/stats/csgo"
    dataX = urllib.request.urlopen(url).read()
    print(dataX)
    
    # tags = soup.find("div", {"class":"key-stat__value text-gray"})
    

    # return f'<h1>LOADED</h1>'





faceit_get(None,None)