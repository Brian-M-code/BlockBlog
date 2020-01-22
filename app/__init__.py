from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from config import config_options

db = SQLAlchemy
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)
mail = Mail()
bootstrap = Bootstrap()
admin = Admin()

def create_app(config_name):
    # App configurations
    app = Flask(__name__)

    # Initialize flask extensions