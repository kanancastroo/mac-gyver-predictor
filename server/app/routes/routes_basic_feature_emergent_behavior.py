from app import app, db
from flask import jsonify, request
from models import Basic_Feature_Emergent_Behavior

@app.route("/add_basic_feature_emergent_behavior")
def add_basic_feature_emergent_behavior():
    feature_id=request.args.get('feature_id')
    emergent_id=request.args.get('emergent_id')
    try:
        basic_feature_emergent_behavior=Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior(
            feature_id=feature_id,
            emergent_id=emergent_id,
        )
        db.session.add(basic_feature_emergent_behavior)
        db.session.commit()
        return "Relation Basic Feature/Emergent Behavior added. relation_id={}".format(basic_feature_emergent_behavior.relation_id)
    except Exception as e:
	    return(str(e))           

@app.route("/list_basic_feature_emergent_behavior")
def list_basic_feature_emergent_behavior():
    try:
        basic_feature_emergent_behavior=Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.query.all()
        return  jsonify([e.serialize() for e in basic_feature_emergent_behavior])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))   

@app.route("/delete_basic_feature_emergent_behavior")
def delete_basic_feature_emergent_behavior():
    relation_id=request.args.get('relation_id')
    try:
        relation = Basic_Feature_Emergent_Behavior.Basic_Feature_Emergent_Behavior.query.filter_by(relation_id=relation_id).one()
        db.session.delete(relation)
        db.session.commit()
        return "Relation id={} was deleted sucessfully".format(relation_id)
    except Exception as e:
	    return(str(e))            