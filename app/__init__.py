from flask import Flask
from config import DevConfig
# from flask_bootstrap import Bootstrap

# Initializing application
def create_app(config_name):
    app = Flask(__name__)

# SETTING UP CONFIGURATION
    app.config.from_object(config_options[config_name])

    return app