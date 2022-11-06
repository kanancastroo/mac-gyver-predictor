from app import app, db
from flask import jsonify, request
import numpy as np
import jsons
from models import Constituent_Basic_Feature, Constituent, Basic_Feature

@app.route("/relation/constituent_basic_feature/add")
def addRelationConstituentBasicFeature():
    constituent_external_id=request.args.get('constituent_external_id')
    feature_external_id=request.args.get('feature_external_id')

    constituent = Constituent.Constituent.query.filter_by(constituent_external_id=constituent_external_id).first()
    basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_external_id=feature_external_id).first()

    try:
        constituent_basic_feature=Constituent_Basic_Feature.Constituent_Basic_Feature(
            basic_feature_id=basic_feature.feature_id,
            constituent_id=constituent.constituent_id,
        )
        db.session.add(constituent_basic_feature)
        db.session.commit()
        # return "Relation SoS/Constituent added. relation_id={}".format(sos_constituent.relation_id)
        return "Relation Constituent/Basic Feature added successfully."
    except Exception as e:
	    return(str(e))          

@app.route("/relation/constituent_basic_feature/delete")
def deleteRelationConstituentBasicFeature():
    constituent_external_id=request.args.get('constituent_external_id')
    feature_external_id=request.args.get('feature_external_id')

    constituent = Constituent.Constituent.query.filter_by(constituent_external_id=constituent_external_id).first()
    basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_external_id=feature_external_id).first()

    try:
        relation = Constituent_Basic_Feature.Constituent_Basic_Feature.query.filter_by(
            constituent_id=constituent.constituent_id,
            basic_feature_id=basic_feature.feature_id
        ).one()

        db.session.delete(relation)
        db.session.commit()
        return "Relation Constituent/Basic Feature deleted successfully."
    except Exception as e:
	    return(str(e))        

@app.route("/relation/constituent_basic_feature/get")
def getRelationsConstituentBasicFeature():
    class ConstituentBasicFeature():
        def __init__(self, constituent_external_id, feature_external_id):
            self.constituent_external_id = constituent_external_id
            self.feature_external_id = feature_external_id

        def toJSON(self):
            return jsons.dump(self) 

    try:
        constituents=request.args.get('constituent_list')
        features=request.args.get('features_list')

        arr_constituent = constituents.split(sep=',')
        constituent_list = np.array(arr_constituent)

        arr_features = features.split(sep=',')
        features_list = np.array(arr_features)        
        
        constituent_objs = Constituent.Constituent.query.filter(Constituent.Constituent.constituent_external_id.in_(constituent_list))
        features_objs = Basic_Feature.Basic_Feature.query.filter(Basic_Feature.Basic_Feature.feature_external_id.in_(features_list))

        relations = []

        for constituent_obj in constituent_objs:
            for features_obj in features_objs:
                    relation = Constituent_Basic_Feature.Constituent_Basic_Feature.query.filter_by(
                        constituent_id=constituent_obj.constituent_id,
                        basic_feature_id=features_obj.feature_id
                    ).all()

                    relations.append(relation)

        constituent_basic_features_relations = []
        print(constituent_basic_features_relations)

        for relation in relations:
            constituent = Constituent.Constituent.query.filter_by(constituent_id=relation.constituent_id).first()
            feature = Basic_Feature.Basic_Feature.query.filter_by(feature_id=relation.feature_id).first()            


            constituent_basic_feature_relation = ConstituentBasicFeature(constituent_external_id=constituent.constituent_external_id, feature_external_id=feature.feature_external_id)
            constituent_basic_features_relations.append(constituent_basic_feature_relation)

        return jsonify([e.toJSON() for e in constituent_basic_features_relations])
    except Exception as e:
	    return(str(e))    