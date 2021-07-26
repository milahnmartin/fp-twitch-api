import requests
from webscraper.keys import my_api_key
# import keys

class Faceit:

    game_id = "csgo"
    api_header = {"Authorization":"Bearer " + my_api_key,"content-type": "application/json"}


    def __init__(self,pname) -> None:
        self.pname = pname
       
        

    def get_player_id(self) -> int:
        try:
            player_id_request = requests.get(f"https://open.faceit.com/data/v4/players?nickname={self.pname}&game=CSGO",headers=self.api_header)
            player_id_data = player_id_request.json()
            player_id = player_id_data["player_id"]
            return player_id
        except KeyError:
            print('Error Occured',self.pname,'doesnt exist')
            return {'status':False}




    def get_player_data(self) -> dict:
        player_data = requests.get(f"https://open.faceit.com/data/v4/players/{self.get_player_id()}",headers=self.api_header)
        player_data_json = player_data.json()
        return player_data_json



    def get_player_stats(self) -> dict:
        player_stats_request = requests.get(f'https://open.faceit.com/data/v4/players/{self.get_player_id()}/stats/{self.game_id}',headers=self.api_header)
        player_stats_json = player_stats_request.json()
        return player_stats_json


    def get_player_map_stats(self,pMap) -> dict:
        player_data = self.get_player_stats()
        segments_data = player_data['segments']
        for i in segments_data:
            if i['label'] == pMap:
                return i

        return {"error":"Map doesnt Exist"}



