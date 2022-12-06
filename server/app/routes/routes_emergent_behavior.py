from app import app, db
from flask import jsonify, request
from models import Emergent_Behavior
import jsons
import numpy as np
import uuid

@app.route("/emergent_behaviors/get")
def getEmergentBehaviors():
    try:
        emergent_behavior=Emergent_Behavior.Emergent_Behavior.query.all()
        return  jsonify([e.serialize() for e in emergent_behavior])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))

@app.route("/emergent_behaviors/add")
def addEmergentBehavior():
    description=request.args.get('description')
    emergent_external_id=request.args.get('emergent_id')
    try:
        emergent_behavior=Emergent_Behavior.Emergent_Behavior(
            emergent_external_id = emergent_external_id,
            description=description,
        )
        db.session.add(emergent_behavior)
        db.session.commit()
        return "Emergent Behavior added. emergent_external_id={}.".format(emergent_behavior.emergent_external_id)
    except Exception as e:
	    return(str(e))    

@app.route("/emergent_behaviors/<emergent_id>/get")
def getEmergentBehavior(emergent_id):
    emergent_external_id=str(emergent_id)
    try:
        emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).first()
        return jsonify(emergent_behavior.description)
    except Exception as e:
	    return(str(e))    

@app.route("/emergent_behaviors/<emergent_id>/update")
def updateEmergentBehavior(emergent_id):
    emergent_external_id=str(emergent_id)
    description=request.args.get('description')
    try:
        emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).first()
        emergent_behavior.description = description
        db.session.commit()
        return "Emergent Behavior updated. emergent_external_id={}.".format(emergent_behavior.emergent_external_id)
    except Exception as e:
	    return(str(e))     

@app.route("/emergent_behaviors/<emergent_id>/delete")
def deleteEmergentBehavior(emergent_id):
    emergent_external_id=str(emergent_id)
    try:
        emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).one()
        db.session.delete(emergent_behavior)
        db.session.commit()
        return "Emergent Behavior id={} was deleted sucessfully.".format(emergent_external_id)
    except Exception as e:
	    return(str(e))    