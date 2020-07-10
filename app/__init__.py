from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):


    # Initializing application
    app = Flask(__name__)

    #set up configuration
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    from .request import configure_request
    configure_request(app)


    return app

