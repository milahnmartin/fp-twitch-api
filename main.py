from flask import Flask
import webscraper

app = Flask(__name__)


@app.route('/get/<string:user_name>/<string:server_name>')
def get(user_name: str, server_name: str) -> str:
    server_name.lower()
    if server_name == 'faceit':
        user_instance = webscraper.Faceit(user_name)
        return user_instance.get_player_stats()
    elif server_name == 'esea':
        return webscraper.esea_get(user_name, category)
    elif server_name == 'hltv':
        return webscraper.hltv_get(user_name, category)
    else:
        return f'<h1>Following Server {server_name} is out of Service ...</h1>'


@app.route('/')
def home()-> dict:
    return {"status":"error","reason":"no url given"}

if __name__ == "__main__":
    app.run()
