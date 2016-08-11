import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config[
    'SECRET_KEY'] = "\xf8\xa3\xbb\xb0I\xc5(v\xa53\x10\x0c\xf9\xf0\x84\xf2z\xcb\x89'\x82u\x7fW"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'termos.db')
app.config['DEBUG'] = True

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

from thermos import models, views
