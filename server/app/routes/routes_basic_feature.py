from app import app, db
from flask import jsonify, request
from models import Basic_Feature

@app.route("/add_basic_feature")
def add_basic_feature():
    description=request.args.get('description')
    try:
        basic_feature=Basic_Feature.Basic_Feature(
            description=description,
        )
        db.session.add(basic_feature)
        db.session.commit()
        return "Basic Feature added. feature_id={}".format(basic_feature.feature_id)
    except Exception as e:
	    return(str(e))    

@app.route("/list_basic_feature")
def list_basic_feature():
    try:
        basic_feature=Basic_Feature.Basic_Feature.query.all()
        return  jsonify([e.serialize() for e in basic_feature])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))          

@app.route("/delete_basic_feature")
def delete_basic_feature():
    feature_id=request.args.get('feature_id')
    try:
        basic_feature = Basic_Feature.Basic_Feature.query.filter_by(feature_id=feature_id).one()
        db.session.delete(basic_feature)
        db.session.commit()
        return "Basic Feature id={} was deleted sucessfully".format(feature_id)
    except Exception as e:
	    return(str(e))   
