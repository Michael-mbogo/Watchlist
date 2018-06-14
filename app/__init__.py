from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])


    #Initializing flask extentions
    bootstrap.init_app(app)

    #redesstering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #settings config
    from .request import config_request
    config_request(app)

    return app
