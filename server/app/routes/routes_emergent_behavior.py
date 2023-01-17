from app import app, db
from flask import jsonify, request, Response
from models import Emergent_Behavior, Basic_Feature_Emergent_Behavior, Basic_Feature, Constituent_Basic_Feature, Constituent
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
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )

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
        # return "Emergent Behavior added. emergent_external_id={}.".format(emergent_behavior.emergent_external_id)
        return jsonify(emergent_behavior.emergent_external_id)
    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )    

@app.route("/emergent_behaviors/<emergent_id>/get")
def getEmergentBehavior(emergent_id):
    emergent_external_id=str(emergent_id)
    try:
        emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).first()
        return jsonify(emergent_behavior.description)
    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )    

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
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )     

@app.route("/emergent_behaviors/<emergent_id>/delete")
def deleteEmergentBehavior(emergent_id):
    emergent_external_id=str(emergent_id)
    try:
        emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).one()
        db.session.delete(emergent_behavior)
        db.session.commit()
        return "Emergent Behavior id={} was deleted sucessfully.".format(emergent_external_id)
    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )    


@app.route("/emergent_behaviors/basic_features/constituents/post", methods=['POST'])
def getConstituentsFromEmergentBehaviors():
    class CS():
        def __init__(self, constituent_external_id, constituent_name):
            self.constituent_external_id = constituent_external_id
            self.constituent_name = constituent_name

        def toJSON(self):
            return jsons.dump(self)

    behavior_elements=request.json['behaviors_list']
    emergent_external_ids = []

    for item in behavior_elements:
        emergent_external_ids.append(item['emergent_external_id'])

    try:
        results = db.session.query(Emergent_Behavior.Emergent_Behavior, Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior, \
        Basic_Feature.Basic_Feature, Constituent_Basic_Feature.Constituent_Basic_Feature, \
        Constituent.Constituent) \
        .select_from(Emergent_Behavior.Emergent_Behavior) \
        .join(Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior, Emergent_Behavior.Emergent_Behavior.emergent_id == Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.emergent_behavior_id) \
        .join(Basic_Feature.Basic_Feature, Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.basic_feature_id == Basic_Feature.Basic_Feature.feature_id) \
        .join(Constituent_Basic_Feature.Constituent_Basic_Feature, Basic_Feature.Basic_Feature.feature_id == Constituent_Basic_Feature.Constituent_Basic_Feature.basic_feature_id) \
        .join(Constituent.Constituent, Constituent_Basic_Feature.Constituent_Basic_Feature.constituent_id == Constituent.Constituent.constituent_id) \
        .filter(Emergent_Behavior.Emergent_Behavior.emergent_external_id.in_((emergent_external_ids))) \
        .distinct().all()

        array_constituents = []
        # print('RESULTS =>>> ', results)

        for emergent_id, relation_id, feature_id, relation_id, constituent_id in results:
            constituent = CS(constituent_external_id=constituent_id.constituent_external_id, constituent_name=constituent_id.constituent_name)
            array_constituents.append(constituent)
            # print(sos_id.sos_name, constituent_id.constituent_id, constituent_id.constituent_name)
            # print(array_constituents)

        seen_ids = set()
        new_list = []
        for obj in array_constituents:
            if obj.constituent_external_id not in seen_ids:
                new_list.append(obj)
                seen_ids.add(obj.constituent_external_id)

        # print('new_list =>>> ', new_list)

        return jsonify([e.toJSON() for e in new_list])

    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )          