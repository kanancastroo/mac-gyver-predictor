from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='../../client/dist/',    static_url_path='/')
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import views