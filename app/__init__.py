from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    # set up configurations
	app.config.from_object(config_options[config_name])

	# initialize flask extensions
	bootstrap.init_app(app)


	# setting config 
	from .request import configure_request
	configure_request(app)

	return app 