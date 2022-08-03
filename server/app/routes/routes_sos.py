from app import app, db
from flask import jsonify, request
from models import SoS

@app.route("/add_sos")
def add_sos():
    sos_name=request.args.get('sos_name')
    try:
        sos=SoS.SoS(
            sos_name=sos_name,
        )
        db.session.add(sos)
        db.session.commit()
        return "SoS added. sos_id={}".format(sos.sos_id)
    except Exception as e:
	    return(str(e))    
        
@app.route("/list_sos")
def list_sos():
    try:
        sos=SoS.SoS.query.all()
        return  jsonify([e.serialize() for e in sos])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))

@app.route("/delete_sos")
def delete_sos():
    sos_id=request.args.get('sos_id')
    try:
        sos = SoS.SoS.query.filter_by(sos_id=sos_id).one()
        db.session.delete(sos)
        db.session.commit()
        return "SoS id={} was deleted sucessfully".format(sos_id)
    except Exception as e:
	    return(str(e))        


    