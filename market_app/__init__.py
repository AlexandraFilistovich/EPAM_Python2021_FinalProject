from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_migrate import Migrate


MIGRATION_DIR = path.join('market_app', 'migrations')
TEMPLATES_DIR = 'templates'

app = Flask(__name__, template_folder=TEMPLATES_DIR)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = '9d48085960843c06a0e26919'
db = SQLAlchemy(app)
migrate = Migrate(app,  db, directory=MIGRATION_DIR)


bcrypt = Bcrypt(app)    
login_manager = LoginManager(app)
login_manager.login_view = 'login_load'

from market_app import views
from .models.user_model import User
from .models.item_model import Item