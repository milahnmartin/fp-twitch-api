from flask import Flask
import webscraper

app = Flask(__name__)


@app.route('/get/<string:user_name>/<string:server_name>/<string:category>')
def request(user_name: str, server_name: str, category: str) -> str:
    if server_name == 'faceit':
        return webscraper.faceit_get(user_name, category)
    elif server_name == 'esea':
        return webscraper.esea_get(user_name, category)
    elif server_name == 'hltv':
        return webscraper.hltv_get(user_name, category)
    else:
        return f'<h1>Following Server {server_name} is out of Service ...</h1>'


if __name__ == "__main__":
    app.run()
