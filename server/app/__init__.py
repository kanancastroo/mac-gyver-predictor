from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import flask_cors
import os

load_dotenv()

app = Flask(__name__, static_folder='../dist/',    static_url_path='/')
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.routes import routes_operational, routes_sos, routes_constituent, routes_basic_feature, routes_emergent_behavior, \
routes_sos_constituent, routes_constituent_basic_feature, routes_basic_feature_emergent_behavior, \
routes_sos_emergent_behavior, routes_processing, routes_user


flask_cors.cross_origin(
origins = '*', 
methods = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT'], 
headers = None, 
supports_credentials = False, 
max_age = None, 
send_wildcard = True, 
always_send = True, 
automatic_options = False
)

#CORS(app, resources={r"/*":{'origins':'*'}})
CORS(app)