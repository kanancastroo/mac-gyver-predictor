from app import app, db
from flask import jsonify, request
from models import SoS_Constituent

@app.route("/add_sos_constituent")
def add_sos_constituent():
    sos_id=request.args.get('sos_id')
    constituent_id=request.args.get('constituent_id')
    try:
        sos_constituent=SoS_Constituent.SoS_Constituent(
            sos_id=sos_id,
            constituent_id=constituent_id,
        )
        db.session.add(sos_constituent)
        db.session.commit()
        return "Relation SoS/Constituent added. relation_id={}".format(sos_constituent.relation_id)
    except Exception as e:
	    return(str(e))           

@app.route("/list_sos_constituents")
def list_sos_constituents():
    try:
        sos_constituents=SoS_Constituent.SoS_Constituent.query.all()
        return  jsonify([e.serialize() for e in sos_constituents])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))   

@app.route("/delete_sos_constituent")
def delete_sos_constituent():
    relation_id=request.args.get('relation_id')
    try:
        relation = SoS_Constituent.SoS_Constituent.query.filter_by(relation_id=relation_id).one()
        db.session.delete(relation)
        db.session.commit()
        return "Relation id={} was deleted sucessfully".format(relation_id)
    except Exception as e:
	    return(str(e))            