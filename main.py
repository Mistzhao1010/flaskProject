import requests
from flask import Flask, request
from router import resgister, api_map
from config import EnvConfig

app = Flask(__name__)


@app.route('/')
def index():
    client_ip = requests.get('https://icanhazip.com/').text
    return client_ip


def init_app(app):
    app.config.from_object(EnvConfig)
    resgister.register_app_routers(app, api_map.routes)


init_app(app)
