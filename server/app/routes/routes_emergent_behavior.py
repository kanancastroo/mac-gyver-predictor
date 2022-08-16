from app import app, db
from flask import jsonify, request
from models import Emergent_Behavior

@app.route("/add_emergent_behavior")
def add_emergent_behavior():
    description=request.args.get('description')
    try:
        emergent_behavior=Emergent_Behavior.Emergent_Behavior(
            description=description,
        )
        db.session.add(emergent_behavior)
        db.session.commit()
        return "Emergent Behavior added. emergent_id={}".format(emergent_behavior.emergent_id)
    except Exception as e:
	    return(str(e))    
        
@app.route("/list_emergent_behavior")
def list_emergent_behavior():
    try:
        emergent_behavior=Emergent_Behavior.Emergent_Behavior.query.all()
        return  jsonify([e.serialize() for e in emergent_behavior])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))

@app.route("/delete_emergent_behavior")
def delete_emergent_behavior():
    emergent_id=request.args.get('emergent_id')
    try:
        emergent_behavior = Emergent_Behavior.Emergent_Behavior.query.filter_by(emergent_id=emergent_id).one()
        db.session.delete(emergent_behavior)
        db.session.commit()
        return "Emergent Behavior id={} was deleted sucessfully".format(emergent_id)
    except Exception as e:
	    return(str(e))     