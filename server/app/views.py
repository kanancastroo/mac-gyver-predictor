from app import app, db
from flask import jsonify, request
from models import SoS

# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/add")
def add_sos():
    name=request.args.get('name')
    try:
        sos=SoS.SoS(
            name=name,
        )
        db.session.add(sos)
        db.session.commit()
        return "SoS added. sos id={}".format(sos.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        sos=SoS.query.all()
        return  jsonify([e.serialize() for e in sos])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))