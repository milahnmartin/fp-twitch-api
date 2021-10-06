from flask import Flask
import webscraper

app = Flask(__name__)


@app.route('/get/<string:user_name>/<string:server_name>/<string:user_map>')
def get(user_name: str, server_name: str,user_map:str) -> dict:

    server_name.lower()
    user_map.lower()
    if server_name == 'faceit' and user_map == 'none':
        user_instance = webscraper.Faceit(user_name)
        return user_instance.get_player_stats()
    elif server_name == 'faceit' and user_map != 'none':
        user_map = "de_"+user_map
        map_instance = webscraper.Faceit(user_name)
        return  map_instance.get_player_map_stats(user_map)
    elif server_name == 'esea':
        return webscraper.esea_get(user_name, user_map)
    elif server_name == 'hltv':
        return webscraper.hltv_get(user_name, user_map)
    else:
        return f'<h1>Following Server {server_name} is out of Service ...</h1>'


@app.route('/')
def home() -> dict:
    return {"status":"error","reason":"no url given"}

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
