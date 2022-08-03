from app import app, db
from flask import jsonify, request
from models import Constituent

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
