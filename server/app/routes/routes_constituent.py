from app import app, db
from flask import jsonify, request
from models import Constituent, Constituent_Basic_Feature, Basic_Feature, Basic_Feature_Emergent_Behavior, Emergent_Behavior
import jsons
import numpy as np

@app.route("/add_constituent")
def add_constituent():
    constituent_name=request.args.get('constituent_name')
    try:
        constituent=Constituent.Constituent(
            constituent_name=constituent_name,
        )
        db.session.add(constituent)
        db.session.commit()
        return "Constituent added. constituent_id={}".format(constituent.constituent_id)
    except Exception as e:
	    return(str(e))    

@app.route("/list_constituents")
def list_constituents():
    try:
        constituent=Constituent.Constituent.query.all()
        return  jsonify([e.serialize() for e in constituent])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))          

@app.route("/delete_constituent")
def delete_constituent():
    constituent_id=request.args.get('constituent_id')
    try:
        constituent = Constituent.Constituent.query.filter_by(constituent_id=constituent_id).one()
        db.session.delete(constituent)
        db.session.commit()
        return "Constituent id={} was deleted sucessfully".format(constituent_id)
    except Exception as e:
	    return(str(e))   

@app.route("/list_emergent_behaviors_from_constituents")
def list_emergent_behaviors_from_constituents():
    class EmergentBehavior():
        def __init__(self, emergent_id, description):
            self.emergent_id = emergent_id
            self.description = description

        def toJSON(self):
            return jsons.dump(self)

    constituent_id=request.args.get('constituent_id')
    aux = constituent_id[1:-1]
    arr = aux.split(sep=',')
    # print(arr)
    constituent_list = np.array(arr)
    # for i in range(len(test)):
    #     print(i, ' IS => ', test[i])
    # test = arr.array('i', test1)
    # print(test)
    try:
        results = db.session.query(Constituent.Constituent, Constituent_Basic_Feature.Constituent_Basic_Feature, \
        Basic_Feature.Basic_Feature, Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior, \
        Emergent_Behavior.Emergent_Behavior) \
        .select_from(Constituent.Constituent) \
        .join(Constituent_Basic_Feature.Constituent_Basic_Feature, Constituent.Constituent.constituent_id == Constituent_Basic_Feature.Constituent_Basic_Feature.constituent_id) \
        .join(Basic_Feature.Basic_Feature, Constituent_Basic_Feature.Constituent_Basic_Feature.basic_feature_id == Basic_Feature.Basic_Feature.feature_id) \
        .join(Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior, Basic_Feature.Basic_Feature.feature_id == Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.basic_feature_id) \
        .join(Emergent_Behavior.Emergent_Behavior, Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.emergent_behavior_id == Emergent_Behavior.Emergent_Behavior.emergent_id) \
        .filter(Constituent.Constituent.constituent_id.in_((constituent_list))) \
        .distinct().all()

        array_emergent_behaviors = []
        print(results)

        for constituent_id, relation_id, feature_id, relation_id, emergent_id in results:
            emergent_behavior = EmergentBehavior(emergent_id=emergent_id.emergent_id, description=emergent_id.description)
            array_emergent_behaviors.append(emergent_behavior)
            # print(sos_id.sos_name, constituent_id.constituent_id, constituent_id.constituent_name)
            # print(array_constituents)

        seen_ids = set()
        new_list = []
        for obj in array_emergent_behaviors:
            if obj.emergent_id not in seen_ids:
                new_list.append(obj)
                seen_ids.add(obj.emergent_id)

        return jsonify([e.toJSON() for e in new_list])
    except Exception as e:
	    return(str(e))  