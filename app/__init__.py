from flask import Flask
from config import config_options

def create_app(config_name):


	# Initializing application
	app = Flask(__name__)

	#set up configuration
	app.config.from_object(config_options[config_name])

	from .request import configure_request
	configure_request(app)


	return app

