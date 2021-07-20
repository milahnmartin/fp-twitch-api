import requests
from requests import api
from requests.api import head
# from webscraper.keys import my_api_key
import keys


class Faceit:

    game_id = "csgo"
    api_header = {"Authorization":"Bearer " + keys.my_api_key,"content-type": "application/json"}


    def __init__(self,pNickname) -> None:
        self.pNickname = pNickname
       
        

    def get_player_id(self):
        player_id_request = requests.get(f"https://open.faceit.com/data/v4/players?nickname={self.pNickname}&game=CSGO",headers=self.api_header)
        player_id_data = player_id_request.json()
        player_id = player_id_data["player_id"]
        return player_id


    def get_player_data(self):
        player_data = requests.get(f"https://open.faceit.com/data/v4/players/{self.get_player_id()}",headers=self.api_header)
        player_data_json = player_data.json()
        print(player_data_json)
    

    def get_player_stats(self):
        player_stats_request = requests.get(f'https://open.faceit.com/data/v4/players/{self.get_player_id()}/stats/{self.game_id}',headers=self.api_header)
        player_stats_json = player_stats_request.json()
        print(player_stats_json)




p = Faceit('Ultrafy')



print(p.get_player_stats())
