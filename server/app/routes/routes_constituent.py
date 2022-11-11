from app import app, db
from flask import jsonify, request
from models import Constituent, Constituent_Basic_Feature, Basic_Feature, Basic_Feature_Emergent_Behavior, Emergent_Behavior
import jsons
import numpy as np
import uuid

@app.route("/constituents/get")
def getConstituents():
    try:
        constituent=Constituent.Constituent.query.all()
        return  jsonify([e.serialize() for e in constituent])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))   

@app.route("/constituents/add")
def addConstituent():
    constituent_name=request.args.get('constituent_name')
    try:
        constituent=Constituent.Constituent(
            constituent_external_id = uuid.uuid4().hex,
            constituent_name=constituent_name,
        )
        db.session.add(constituent)
        db.session.commit()
        return "Constituent added. constituent_external_id={}.".format(constituent.constituent_external_id)
    except Exception as e:
	    return(str(e))  

@app.route("/constituents/<constituent_id>/get")
def getConstituent(constituent_id):
    constituent_external_id=str(constituent_id)
    try:
        constituent = Constituent.Constituent.query.filter_by(constituent_external_id=constituent_external_id).first()
        return jsonify(constituent.constituent_name)
    except Exception as e:
	    return(str(e))    

@app.route("/constituents/<constituent_id>/update")
def updateConstituent(constituent_id):
    constituent_external_id=str(constituent_id)
    constituent_name=request.args.get('constituent_name')
    try:
        constituent = Constituent.Constituent.query.filter_by(constituent_external_id=constituent_external_id).first()
        constituent.constituent_name = constituent_name
        db.session.commit()
        return "Constituent updated. constituent_external_id={}.".format(constituent.constituent_external_id)
    except Exception as e:
	    return(str(e))     

@app.route("/constituents/<constituent_id>/delete")
def deleteConstituent(constituent_id):
    constituent_external_id=str(constituent_id)
    try:
        constituent = Constituent.Constituent.query.filter_by(constituent_external_id=constituent_external_id).one()
        db.session.delete(constituent)
        db.session.commit()
        return "Constituent id={} was deleted sucessfully.".format(constituent_external_id)
    except Exception as e:
	    return(str(e))   

@app.route("/constituents/basic_features/post", methods=['POST'])
def getBasicFeaturesFromConstituents():
    class BasicFeature():
        def __init__(self, feature_external_id, description):
            self.feature_external_id = feature_external_id
            self.description = description

        def toJSON(self):
            return jsons.dump(self)

    constituents_elements=request.json['constituent_list']
    constituents_external_ids = []

    for item in constituents_elements:
        constituents_external_ids.append(item['constituent_external_id'])

    try:
        results = db.session.query(Constituent.Constituent, Constituent_Basic_Feature.Constituent_Basic_Feature, \
        Basic_Feature.Basic_Feature) \
        .select_from(Constituent.Constituent) \
        .join(Constituent_Basic_Feature.Constituent_Basic_Feature, Constituent.Constituent.constituent_id == Constituent_Basic_Feature.Constituent_Basic_Feature.constituent_id) \
        .join(Basic_Feature.Basic_Feature, Constituent_Basic_Feature.Constituent_Basic_Feature.basic_feature_id == Basic_Feature.Basic_Feature.feature_id) \
        .filter(Constituent.Constituent.constituent_external_id.in_((constituents_external_ids))) \
        .distinct().all()

        array_basic_features = []

        for constituent_id, relation_id, feature_id in results:
            basic_feature = BasicFeature(feature_external_id=feature_id.feature_external_id, description=feature_id.description)
            array_basic_features.append(basic_feature)
            # print(sos_id.sos_name, constituent_id.constituent_id, constituent_id.constituent_name)
            # print(array_constituents)

        seen_ids = set()
        new_list = []
        for obj in array_basic_features:
            if obj.feature_external_id not in seen_ids:
                new_list.append(obj)
                seen_ids.add(obj.feature_external_id)

        return jsonify([e.toJSON() for e in new_list])
    except Exception as e:
	    return(str(e))  

# @app.route("/list_emergent_behaviors_from_constituents")
# def list_emergent_behaviors_from_constituents():
#     class EmergentBehavior():
#         def __init__(self, emergent_id, description):
#             self.emergent_id = emergent_id
#             self.description = description

#         def toJSON(self):
#             return jsons.dump(self)

#     constituent_id=request.args.get('constituent_id')
#     aux = constituent_id[1:-1]
#     arr = aux.split(sep=',')
#     # print(arr)
#     constituent_list = np.array(arr)
#     # for i in range(len(test)):
#     #     print(i, ' IS => ', test[i])
#     # test = arr.array('i', test1)
#     # print(test)
#     try:
#         results = db.session.query(Constituent.Constituent, Constituent_Basic_Feature.Constituent_Basic_Feature, \
#         Basic_Feature.Basic_Feature, Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior, \
#         Emergent_Behavior.Emergent_Behavior) \
#         .select_from(Constituent.Constituent) \
#         .join(Constituent_Basic_Feature.Constituent_Basic_Feature, Constituent.Constituent.constituent_id == Constituent_Basic_Feature.Constituent_Basic_Feature.constituent_id) \
#         .join(Basic_Feature.Basic_Feature, Constituent_Basic_Feature.Constituent_Basic_Feature.basic_feature_id == Basic_Feature.Basic_Feature.feature_id) \
#         .join(Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior, Basic_Feature.Basic_Feature.feature_id == Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.basic_feature_id) \
#         .join(Emergent_Behavior.Emergent_Behavior, Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.emergent_behavior_id == Emergent_Behavior.Emergent_Behavior.emergent_id) \
#         .filter(Constituent.Constituent.constituent_id.in_((constituent_list))) \
#         .distinct().all()

#         array_emergent_behaviors = []
#         print(results)

#         for constituent_id, relation_id, feature_id, relation_id, emergent_id in results:
#             emergent_behavior = EmergentBehavior(emergent_id=emergent_id.emergent_id, description=emergent_id.description)
#             array_emergent_behaviors.append(emergent_behavior)
#             # print(sos_id.sos_name, constituent_id.constituent_id, constituent_id.constituent_name)
#             # print(array_constituents)

#         seen_ids = set()
#         new_list = []
#         for obj in array_emergent_behaviors:
#             if obj.emergent_id not in seen_ids:
#                 new_list.append(obj)
#                 seen_ids.add(obj.emergent_id)

#         return jsonify([e.toJSON() for e in new_list])
#     except Exception as e:
# 	    return(str(e))  