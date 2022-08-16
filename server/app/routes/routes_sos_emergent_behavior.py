from app import app, db
from flask import jsonify, request
from models import SoS_Emergent_Behavior

@app.route("/add_sos_emergent_behavior")
def add_sos_emergent_behavior():
    sos_id=request.args.get('sos_id')
    emergent_id=request.args.get('emergent_id')
    try:
        sos_emergent_behavior=SoS_Emergent_Behavior.SoS_Emergent_Behavior(
            sos_id=sos_id,
            emergent_id=emergent_id,
        )
        db.session.add(sos_emergent_behavior)
        db.session.commit()
        return "Relation SoS/Emergent Behavior added. relation_id={}".format(sos_emergent_behavior.relation_id)
    except Exception as e:
	    return(str(e))           

@app.route("/list_sos_emergent_behavior")
def list_sos_emergent_behavior():
    try:
        sos_emergent_behavior=SoS_Emergent_Behavior.SoS_Emergent_Behavior.query.all()
        return  jsonify([e.serialize() for e in sos_emergent_behavior])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))   

@app.route("/delete_sos_emergent_behavior")
def delete_sos_emergent_behavior():
    relation_id=request.args.get('relation_id')
    try:
        relation = SoS_Emergent_Behavior.SoS_Emergent_Behavior.query.filter_by(relation_id=relation_id).one()
        db.session.delete(relation)
        db.session.commit()
        return "Relation id={} was deleted sucessfully".format(relation_id)
    except Exception as e:
	    return(str(e))   