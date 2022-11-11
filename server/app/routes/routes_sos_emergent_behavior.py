from app import app, db
from flask import jsonify, request
import numpy as np
import jsons
from models import SoS_Emergent_Behavior, SoS, Emergent_Behavior

@app.route("/relation/sos_emergent_behavior/add", methods=['GET', 'POST'])
def addRelationSoSEmergentBehavior():
    if request.method == 'POST':
        sos_external_id=request.json['sos_external_id']
        emergent_behaviors_list=request.json['emergent_behaviors_list']

        # print(len(basic_features_list))
        # print(len(emergent_behaviors_list))
        items = []
        i = 0

        for behavior in emergent_behaviors_list:
            print('i: ', i)
            print(sos_external_id)
            print(behavior['emergent_external_id'])
            sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).first()
            emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=behavior['emergent_external_id']).first()
            
            sos_emergent_behavior=SoS_Emergent_Behavior.SoS_Emergent_Behavior(
                sos_id=sos.sos_id,
                emergent_behavior_id=emergent_behavior.emergent_id,
            )

            items.append(sos_emergent_behavior)
            # db.session.add(basic_feature_emergent_behavior)


            i = i + 1
            
        db.session.add_all(items)
        db.session.commit()
    
        return "Relations SoS/Emergent Behavior added successfully."

    else:
        emergent_external_id=request.args.get('emergent_external_id')
        sos_external_id=request.args.get('sos_external_id')

        emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).first()
        sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).first()

        try:
            sos_emergent_behavior=SoS_Emergent_Behavior.SoS_Emergent_Behavior(
                emergent_behavior_id=emergent_behavior.emergent_id,
                sos_id=sos.sos_id
            )
            db.session.add(sos_emergent_behavior)
            db.session.commit()
            # return "Relation SoS/Constituent added. relation_id={}".format(sos_constituent.relation_id)
            return "Relation SoS/Emergent Behavior added successfully."
        except Exception as e:
            return(str(e))        


@app.route("/relation/sos_emergent_behavior/delete")
def deleteRelationSoSEmergentBehavior():
    emergent_external_id=request.args.get('emergent_external_id')
    sos_external_id=request.args.get('sos_external_id')

    emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_external_id=emergent_external_id).first()
    sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).first()

    try:
        relation = SoS_Emergent_Behavior.SoS_Emergent_Behavior.query.filter_by(
            emergent_behavior_id=emergent_behavior.emergent_id,
            sos_id=sos.sos_id
        ).one()

        db.session.delete(relation)
        db.session.commit()
        return "Relation SoS/Emergent Behavior deleted successfully."
    except Exception as e:
	    return(str(e))        

@app.route("/relation/sos_emergent_behavior/get")
def getRelationsSoSEmergentBehavior():
    class SoSEmergentBehavior():
        def __init__(self, sos_external_id, emergent_external_id):
            self.sos_external_id = sos_external_id
            self.emergent_external_id = emergent_external_id

        def toJSON(self):
            return jsons.dump(self) 

    try:
        sos=request.args.get('sos_list')
        emergents=request.args.get('emergents_list')

        arr_sos = sos.split(sep=',')
        sos_list = np.array(arr_sos)    

        arr_emergents = emergents.split(sep=',')
        emergents_list = np.array(arr_emergents)              
        
        sos_objs = SoS.SoS.query.filter(SoS.SoS.sos_external_id.in_(sos_list))
        emergents_objs = Emergent_Behavior.Emergent_Behavior.query.filter(Emergent_Behavior.Emergent_Behavior.emergent_external_id.in_(emergents_list))

        relations = []

        for sos_obj in sos_objs:
            for emergents_obj in emergents_objs:
                    relation = SoS_Emergent_Behavior.SoS_Emergent_Behavior.query.filter_by(
                        sos_id=sos_obj.sos_id,
                        emergent_behavior_id=emergents_obj.emergent_id
                    ).first()

                    relations.append(relation)

        relations = [x for x in relations if x != None]

        sos_emergent_behaviors_relations = []

        for relation in relations:
            sos = SoS.SoS.query.filter_by(sos_id=relation.sos_id).first()  
            emergent = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_id=relation.emergent_behavior_id).first()            

            sos_emergent_behavior_relation = SoSEmergentBehavior(sos_external_id=sos.sos_external_id, emergent_external_id=emergent.emergent_external_id)
            sos_emergent_behaviors_relations.append(sos_emergent_behavior_relation)

        return jsonify([e.toJSON() for e in sos_emergent_behaviors_relations])
    except Exception as e:
	    return(str(e))    