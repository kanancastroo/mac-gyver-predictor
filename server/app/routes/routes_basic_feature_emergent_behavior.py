from app import app, db
from flask import jsonify, request
import numpy as np
import jsons
from models import Basic_Feature_Emergent_Behavior, Basic_Feature, Emergent_Behavior

@app.route("/relation/basic_feature_emergent_behavior/add", methods=['GET', 'POST'])
def addRelationBasicFeatureEmergentBehavior():
    if request.method == 'POST':
        basic_features_list=request.json['basic_features_list']
        emergent_behaviors_list=request.json['emergent_behaviors_list']

        # print(len(basic_features_list))
        # print(len(emergent_behaviors_list))
        try:
            items = []
            i = 0
            for behavior in emergent_behaviors_list:
                j = 0
                for feature in basic_features_list:
                    print('i: ', i, 'j: ', j)
                    print(feature['feature_external_id'])
                    print(behavior['emergent_external_id'])
                    basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_external_id=feature['feature_external_id']).first()
                    emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=behavior['emergent_external_id']).first()
                    
                    basic_feature_emergent_behavior=Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior(
                        basic_feature_id=basic_feature.feature_id,
                        emergent_behavior_id=emergent_behavior.emergent_id,
                    )

                    items.append(basic_feature_emergent_behavior)
                    # db.session.add(basic_feature_emergent_behavior)
                    j = j + 1

                i = i + 1
                
            db.session.add_all(items)
            db.session.commit()
        
            return "Relations Basic Feature/Emergent Behavior added successfully."
        except Exception as e:
            return(str(e))  

    else:
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

@app.route("/relation/basic_feature_emergent_behavior/post", methods=['POST'])
def getRelationsBasicFeatureEmergentBehavior():
    class BasicFeatureEmergentBehavior():
        def __init__(self, feature_external_id, emergent_external_id):
            self.feature_external_id = feature_external_id
            self.emergent_external_id = emergent_external_id

        def toJSON(self):
            return jsons.dump(self) 

    try:
        features=request.json['features_list']
        emergents=request.json['emergents_list']
        
        features_list = []
        emergents_list = []

        for item in features:
            features_list.append(item['feature_external_id'])  

        for item in emergents:
            emergents_list.append(item['emergent_external_id'])  
            
        
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