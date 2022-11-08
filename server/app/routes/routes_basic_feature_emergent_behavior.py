from app import app, db
from flask import jsonify, request
import numpy as np
import jsons
from models import Basic_Feature_Emergent_Behavior, Basic_Feature, Emergent_Behavior

@app.route("/relation/basic_feature_emergent_behavior/add")
def addRelationBasicFeatureEmergentBehavior():
    feature_external_id=request.args.get('feature_external_id')
    emergent_external_id=request.args.get('emergent_external_id')

    basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_external_id=feature_external_id).first()
    emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).first()

    try:
        basic_feature_emergent_behavior=Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior(
            basic_feature_id=basic_feature.feature_id,
            emergent_behavior_id=emergent_behavior.emergent_id,
        )
        db.session.add(basic_feature_emergent_behavior)
        db.session.commit()
        # return "Relation SoS/Constituent added. relation_id={}".format(sos_constituent.relation_id)
        return "Relation Basic Feature/Emergent Behavior added successfully."
    except Exception as e:
	    return(str(e))        


@app.route("/relation/basic_feature_emergent_behavior/delete")
def deleteRelationBasicFeatureEmergentBehavior():
    feature_external_id=request.args.get('feature_external_id')
    emergent_external_id=request.args.get('emergent_external_id')

    basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_external_id=feature_external_id).first()
    emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).first()

    try:
        relation = Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.query.filter_by(
            emergent_behavior_id=emergent_behavior.emergent_id,
            basic_feature_id=basic_feature.feature_id
        ).one()

        db.session.delete(relation)
        db.session.commit()
        return "Relation Basic Feature/Emergent Behavior deleted successfully."
    except Exception as e:
	    return(str(e))        

@app.route("/relation/basic_feature_emergent_behavior/get")
def getRelationsBasicFeatureEmergentBehavior():
    class BasicFeatureEmergentBehavior():
        def __init__(self, feature_external_id, emergent_external_id):
            self.feature_external_id = feature_external_id
            self.emergent_external_id = emergent_external_id

        def toJSON(self):
            return jsons.dump(self) 

    try:
        features=request.args.get('features_list')
        emergents=request.args.get('emergents_list')

        arr_features = features.split(sep=',')
        features_list = np.array(arr_features)    

        arr_emergents = emergents.split(sep=',')
        emergents_list = np.array(arr_emergents)              
        
        features_objs = Basic_Feature.Basic_Feature.query.filter(Basic_Feature.Basic_Feature.feature_external_id.in_(features_list))
        emergents_objs = Emergent_Behavior.Emergent_Behavior.query.filter(Emergent_Behavior.Emergent_Behavior.emergent_external_id.in_(emergents_list))

        relations = []

        for features_obj in features_objs:
            for emergents_obj in emergents_objs:
                    relation = Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.query.filter_by(
                        basic_feature_id=features_obj.feature_id,
                        emergent_behavior_id=emergents_obj.emergent_id
                    ).first()

                    relations.append(relation)

        relations = [x for x in relations if x != None]

        basic_features_emergent_behaviors_relations = []

        for relation in relations:
            feature = Basic_Feature.Basic_Feature.query.filter_by(feature_id=relation.basic_feature_id).first()  
            emergent = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_id=relation.emergent_behavior_id).first()            

            basic_feature_emergent_behavior_relation = BasicFeatureEmergentBehavior(feature_external_id=feature.feature_external_id, emergent_external_id=emergent.emergent_external_id)
            basic_features_emergent_behaviors_relations.append(basic_feature_emergent_behavior_relation)

        return jsonify([e.toJSON() for e in basic_features_emergent_behaviors_relations])
    except Exception as e:
	    return(str(e))    