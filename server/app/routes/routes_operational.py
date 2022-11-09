from app import app, db
from flask import jsonify, request
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text
from models import SoS, Constituent, Basic_Feature, Emergent_Behavior, SoS_Constituent, Constituent_Basic_Feature, Basic_Feature_Emergent_Behavior, SoS_Emergent_Behavior
import os

load_dotenv()

# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/database/reset')
def resetDatabase():
    try:
        delete_sos = db.session.query(SoS.SoS).delete()
        delete_constituent = db.session.query(Constituent.Constituent).delete()
        delete_basic_feature = db.session.query(Basic_Feature.Basic_Feature).delete()
        delete_emergent_behavior = db.session.query(Emergent_Behavior.Emergent_Behavior).delete()
        delete_sos_constituent = db.session.query(SoS_Constituent.SoS_Constituent).delete()
        delete_constituent_basic_feature = db.session.query(Constituent_Basic_Feature.Constituent_Basic_Feature).delete()
        delete_basic_feature_emergent_behavior = db.session.query(Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior).delete()
        delete_sos_emergent_behavior = db.session.query(SoS_Emergent_Behavior.SoS_Emergent_Behavior).delete()
        db.session.commit()

        ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..'))
        initial_dataset = os.path.join(ROOT_DIR, 'sql_scripts', 'initial_dataset.sql')
        engine = create_engine(os.environ.get('DATABASE_URL'))
        with engine.connect() as con:
            with open(initial_dataset) as file:
                query = text(file.read())
                con.execute(query)
        
        return jsonify('Database reseted sucessfully!')  
    except Exception as e:
        db.session.rollback()
        return(str(e))  

     