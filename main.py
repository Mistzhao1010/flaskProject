import requests
from router import resgister, api_map
from config import EnvConfig
from utils.flask_app import FlaskApp

app = FlaskApp(import_name=__name__)


@app.route('/')
def index():
    client_ip = requests.get('https://icanhazip.com/').text
    return client_ip


def init_app(app):
    app.config.from_object(EnvConfig)
    resgister.register_app_routers(app, api_map.routes)


init_app(app)
