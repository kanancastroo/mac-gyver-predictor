from app import app, db
from flask import jsonify, request
from models import Constituent_Basic_Feature

@app.route("/add_constituent_basic_feature")
def add_constituent_basic_feature():
    feature_id=request.args.get('feature_id')
    constituent_id=request.args.get('constituent_id')
    try:
        constituent_basic_feature=Constituent_Basic_Feature.Constituent_Basic_Feature(
            feature_id=feature_id,
            constituent_id=constituent_id,
        )
        db.session.add(constituent_basic_feature)
        db.session.commit()
        return "Relation Constituent/Basic Feature added. relation_id={}".format(constituent_basic_feature.relation_id)
    except Exception as e:
	    return(str(e))           

@app.route("/list_constituent_basic_feature")
def list_constituent_basic_feature():
    try:
        constituent_basic_feature=Constituent_Basic_Feature.Constituent_Basic_Feature.query.all()
        return  jsonify([e.serialize() for e in constituent_basic_feature])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))   

@app.route("/delete_constituent_basic_feature")
def delete_constituent_basic_feature():
    relation_id=request.args.get('relation_id')
    try:
        relation = Constituent_Basic_Feature.Constituent_Basic_Feature.query.filter_by(relation_id=relation_id).one()
        db.session.delete(relation)
        db.session.commit()
        return "Relation id={} was deleted sucessfully".format(relation_id)
    except Exception as e:
	    return(str(e))            