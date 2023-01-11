from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__, static_folder='../../client/dist/',    static_url_path='/')
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.routes import routes_operational, routes_sos, routes_constituent, routes_basic_feature, routes_emergent_behavior, \
routes_sos_constituent, routes_constituent_basic_feature, routes_basic_feature_emergent_behavior, \
routes_sos_emergent_behavior, routes_processing, routes_user

CORS(app, resources={r"/*":{'origins':'*'}})