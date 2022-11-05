from app import app, db
from flask import jsonify, request
from models import SoS, Constituent, SoS_Constituent

@app.route("/relation/sos_constituent/add")
def addRelationSoSConstituent():
    sos_external_id=request.args.get('sos_external_id')
    constituent_external_id=request.args.get('constituent_external_id')

    sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).first()
    constituent = Constituent.Constituent.query.filter_by(constituent_external_id=constituent_external_id).first()

    try:
        sos_constituent=SoS_Constituent.SoS_Constituent(
            sos_id=sos.sos_id,
            constituent_id=constituent.constituent_id,
        )
        db.session.add(sos_constituent)
        db.session.commit()
        # return "Relation SoS/Constituent added. relation_id={}".format(sos_constituent.relation_id)
        return "Relation SoS/Constituent added successfully."
    except Exception as e:
	    return(str(e))           

@app.route("/relation/sos_constituent/delete")
def deleteRelationSoSConstituent():
    sos_external_id=request.args.get('sos_external_id')
    constituent_external_id=request.args.get('constituent_external_id')

    sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).first()
    constituent = Constituent.Constituent.query.filter_by(constituent_external_id=constituent_external_id).first()

    try:
        relation = SoS_Constituent.SoS_Constituent.query.filter_by(
            sos_id=sos.sos_id,
            constituent_id=constituent.constituent_id
        ).one()

        db.session.delete(relation)
        db.session.commit()
        return "Relation SoS/Constituent deleted successfully."
    except Exception as e:
	    return(str(e))   



# @app.route("/list_sos_constituents")
# def list_sos_constituents():
#     try:
#         sos_constituents=SoS_Constituent.SoS_Constituent.query.all()
#         return  jsonify([e.serialize() for e in sos_constituents])
#         #return jsonify('HELL YEAH!')
#     except Exception as e:
# 	    return(str(e))            