from app import app, db
from flask import jsonify, request, Response
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text
from models import SoS, Constituent, Basic_Feature, Emergent_Behavior, SoS_Constituent, Constituent_Basic_Feature, Basic_Feature_Emergent_Behavior, SoS_Emergent_Behavior
import os

from sqlalchemy.ext.serializer import loads, dumps
import base64

import io
from datetime import datetime
from flask import request, jsonify, send_file

import time
from io import BytesIO
import zipfile
import os
from flask import send_file

import pathlib
from pathlib import Path

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

def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

@app.route('/database/dump', methods=['POST'])
def dumpDatabase():
    try:
        files = []
        ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
        temp_path = pathlib.Path(os.path.join(ROOT_DIR, 'shared', 'temp'))

        if temp_path.is_dir():
            rm_tree(temp_path)

        temp_path.mkdir(parents=True, exist_ok=True)

        dump_sos_path = pathlib.Path(os.path.join(temp_path, 'dump_sos'))
        dump_constituent_path = pathlib.Path(os.path.join(temp_path, 'dump_constituent'))
        dump_basicFeature_path = pathlib.Path(os.path.join(temp_path, 'dump_basicFeature'))
        dump_emergentBehavior_path = pathlib.Path(os.path.join(temp_path, 'dump_emergentBehavior'))
        dump_sosConstituent_path = pathlib.Path(os.path.join(temp_path, 'dump_sosConstituent'))
        dump_constituentBasicFeature_path = pathlib.Path(os.path.join(temp_path, 'dump_constituentBasicFeature'))
        dump_basicFeatureEmergentBehavior_path = pathlib.Path(os.path.join(temp_path, 'dump_basicFeatureEmergentBehavior'))
        dump_sosEmergentBehavior_path = pathlib.Path(os.path.join(temp_path, 'dump_sosEmergentBehavior'))

        with open(dump_sos_path, 'wb') as dump_sos:
            dump_sos.write(dumps(db.session.query(SoS.SoS).all()))
            files.append(dump_sos_path)
        with open(dump_constituent_path, 'wb') as dump_constituent:
            dump_constituent.write(dumps(db.session.query(Constituent.Constituent).all()))
            files.append(dump_constituent_path)
        with open(dump_basicFeature_path, 'wb') as dump_basicFeature:
            dump_basicFeature.write(dumps(db.session.query(Basic_Feature.Basic_Feature).all()))
            files.append(dump_basicFeature_path)
        with open(dump_emergentBehavior_path, 'wb') as dump_emergentBehavior:
            dump_emergentBehavior.write(dumps(db.session.query(Emergent_Behavior.Emergent_Behavior).all()))
            files.append(dump_emergentBehavior_path)
        with open(dump_sosConstituent_path, 'wb') as dump_sosConstituent:
            dump_sosConstituent.write(dumps(db.session.query(SoS_Constituent.SoS_Constituent).all()))
            files.append(dump_sosConstituent_path)
        with open(dump_constituentBasicFeature_path, 'wb') as dump_constituentBasicFeature:
            dump_constituentBasicFeature.write(dumps(db.session.query(Constituent_Basic_Feature.Constituent_Basic_Feature).all()))
            files.append(dump_constituentBasicFeature_path)
        with open(dump_basicFeatureEmergentBehavior_path, 'wb') as dump_basicFeatureEmergentBehavior:
            dump_basicFeatureEmergentBehavior.write(dumps(db.session.query(Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior).all()))
            files.append(dump_basicFeatureEmergentBehavior_path)
        with open(dump_sosEmergentBehavior_path, 'wb') as dump_sosEmergentBehavior:
            dump_sosEmergentBehavior.write(dumps(db.session.query(SoS_Emergent_Behavior.SoS_Emergent_Behavior).all()))
            files.append(dump_sosEmergentBehavior_path)

        timestr = time.strftime("%Y%m%d-%H%M%S")
        fileName = "dump_{}.zip".format(timestr)

        dump_file = pathlib.Path(os.path.join(temp_path, fileName))
        # memory_file = BytesIO()
        # file_path = '/'
        with zipfile.ZipFile(dump_file, 'a', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                zipf.write(file)
        # memory_file.seek(0)

        print(dump_file)

        return send_file(dump_file,
                     attachment_filename=fileName,
                     as_attachment=True)
    
    except Exception as e:
        return Response(
                "Internal Server Error",
                status=500,
            )    


@app.route('/database/restore', methods=['POST'])
def restoreDatabase():
    try:
        print('loading file...')
        # f = request.files["file"]
        files = request.files.getlist('file')
        print('files => ', files)

        for f in files:
            for row in loads(f.read()):
                # print('row => ', row)
                db.session.merge(row)

        db.session.commit()
        
        return 'Database restored successfully!'
    
    except Exception as e:
        return Response(
                "Internal Server Error",
                status=500,
            )  


@app.route('/database/drop')
def dropDatabase():
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
        
        return 'Database dropped successfully!'
    
    except Exception as e:
        return Response(
                "Internal Server Error",
                status=500,
            )  

@app.route('/database/saveall', methods=['POST'])
def saveEntireDirectory():            
    ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
    shared_folder = pathlib.Path(os.path.join(ROOT_DIR, 'shared'))

    timestr = time.strftime("%Y%m%d-%H%M%S")
    fileName = "shared_folder_{}.zip".format(timestr)
    memory_file = BytesIO()

    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(shared_folder):
            for file in files:
                zipf.write(os.path.join(root, file))
    memory_file.seek(0)
    return send_file(memory_file,
                     attachment_filename=fileName,
                     as_attachment=True)    