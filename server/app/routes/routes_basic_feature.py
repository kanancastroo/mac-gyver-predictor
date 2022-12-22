from app import app, db
from flask import jsonify, request, Response
from models import Basic_Feature
import jsons
import numpy as np
import uuid

@app.route("/basic_features/get")
def getBasicFeatures():
    try:
        basic_feature=Basic_Feature.Basic_Feature.query.all()
        return  jsonify([e.serialize() for e in basic_feature])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return Response(
                "Internal Server Error",
                status=500,
            )  

@app.route("/basic_features/add")
def addBasicFeatures():
    description=request.args.get('description')
    feature_external_id=request.args.get('feature_id')
    try:
        basic_feature=Basic_Feature.Basic_Feature(
            feature_external_id = feature_external_id,
            description=description,
        )
        db.session.add(basic_feature)
        db.session.commit()
        return "Basic Feature added. feature_external_id={}.".format(basic_feature.feature_external_id)
    except Exception as e:
	    return Response(
                "Internal Server Error",
                status=500,
            )           

@app.route("/basic_features/<feature_id>/get")
def getBasicFeature(feature_id):
    feature_external_id=str(feature_id)
    try:
        basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_external_id=feature_external_id).first()
        return jsonify(basic_feature.description)
    except Exception as e:
	    return Response(
                "Internal Server Error",
                status=500,
            )    

@app.route("/basic_features/<feature_id>/update")
def updateBasicFeature(feature_id):
    feature_external_id=str(feature_id)
    description=request.args.get('description')
    try:
        basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_external_id=feature_external_id).first()
        basic_feature.description = description
        db.session.commit()
        return "Basic Feature updated. feature_external_id={}.".format(basic_feature.feature_external_id)
    except Exception as e:
	    return Response(
                "Internal Server Error",
                status=500,
            )     

@app.route("/basic_features/<feature_id>/delete")
def deleteBasicFeature(feature_id):
    feature_external_id=str(feature_id)
    try:
        basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_external_id=feature_external_id).one()
        db.session.delete(basic_feature)
        db.session.commit()
        return "Basic Feature id={} was deleted sucessfully.".format(feature_external_id)
    except Exception as e:
	    return Response(
                "Internal Server Error",
                status=500,
            )    
