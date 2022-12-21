from app import app, db
from flask import jsonify, request, Response
import numpy as np
import jsons
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
	    return Response(
                "Internal Server Error",
                status=500,
            )          

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
	    return Response(
                "Internal Server Error",
                status=500,
            )   

@app.route("/relation/sos_constituent/get")
def getRelationsSoSConstituent():
    class SoSConstituent():
        def __init__(self, sos_external_id, constituent_external_id):
            self.sos_external_id = sos_external_id
            self.constituent_external_id = constituent_external_id

        def toJSON(self):
            return jsons.dump(self) 

    try:
        sos=request.args.get('sos_list')
        constituents=request.args.get('constituent_list')

        arr_sos = sos.split(sep=',')
        sos_list = np.array(arr_sos)

        arr_constituent = constituents.split(sep=',')
        constituent_list = np.array(arr_constituent)
        
        sos_objs = SoS.SoS.query.filter(SoS.SoS.sos_external_id.in_(sos_list)).all()
        constituent_objs = Constituent.Constituent.query.filter(Constituent.Constituent.constituent_external_id.in_(constituent_list))

        relations = []

        for sos_obj in sos_objs:
            for constituent_obj in constituent_objs:
                        relation = SoS_Constituent.SoS_Constituent.query.filter_by(
                            sos_id=sos_obj.sos_id,
                            constituent_id=constituent_obj.constituent_id
                        ).one()

                        relations.append(relation)

        sos_constituent_relations = []

        for relation in relations:
            sos = SoS.SoS.query.filter_by(sos_id=relation.sos_id).first()
            constituent = Constituent.Constituent.query.filter_by(constituent_id=relation.constituent_id).first()

            sos_constituent_relation = SoSConstituent(sos_external_id=sos.sos_external_id, constituent_external_id=constituent.constituent_external_id)
            sos_constituent_relations.append(sos_constituent_relation)

        return jsonify([e.toJSON() for e in sos_constituent_relations])
    except Exception as e:
	    return Response(
                "Internal Server Error",
                status=500,
            )  