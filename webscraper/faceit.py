import requests
# from webscraper.keys import my_api_key
import keys





def faceit_get(pUser:str,pCategory:str) -> None:
    h = {"Authorization":"Bearer " + keys.my_api_key,"content-type": "application/json"}
    response = requests.get(f"https://open.faceit.com/data/v4/players?nickname={pUser}&game=CSGO",headers=h)
    api_response = response.json()
    player_id = api_response['player_id']
    stats_request = requests.get(f"")
    print(player_id)


faceit_get('Ultrafy','Kills')