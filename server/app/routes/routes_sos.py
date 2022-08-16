from app import app, db
from flask import jsonify, request
from models import SoS, SoS_Constituent, Constituent
from sqlalchemy import update
import jsons
import numpy as np
import array as arr

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
    sos_id=request.args.get('sos_id')
    try:
        sos = SoS.SoS.query.filter_by(sos_id=sos_id).first()
        return jsonify(sos.sos_name)
    except Exception as e:
	    return(str(e))           

@app.route("/list_all_sos")
def list_all_sos():
    try:
        sos=SoS.SoS.query.all()
        return  jsonify([e.serialize() for e in sos])
        #return jsonify('HELL YEAH!')
    except Exception as e:
	    return(str(e))          

@app.route("/update_sos")
def update_sos():
    sos_name=request.args.get('sos_name')
    sos_id=request.args.get('sos_id')
    try:
        sos = SoS.SoS.query.filter_by(sos_id=sos_id).first()
        sos.sos_name = sos_name
        db.session.commit()
        return "SoS updated. sos_id={}".format(sos.sos_id)
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


@app.route("/list_constituents_from_sos")
def list_constituents_from_sos():
    class CS():
        def __init__(self, constituent_id, constituent_name):
            self.constituent_id = constituent_id
            self.constituent_name = constituent_name

        def toJSON(self):
            return jsons.dump(self)

    sos_id=request.args.get('sos_id')
    aux = sos_id[1:-1]
    arr = aux.split(sep=',')
    # print(arr)
    sos_list = np.array(arr)
    # for i in range(len(test)):
    #     print(i, ' IS => ', test[i])
    # test = arr.array('i', test1)
    # print(test)
    try:
        results = db.session.query(SoS.SoS, SoS_Constituent.SoS_Constituent, Constituent.Constituent) \
        .select_from(SoS.SoS) \
        .join(SoS_Constituent.SoS_Constituent, SoS.SoS.sos_id == SoS_Constituent.SoS_Constituent.sos_id) \
        .join(Constituent.Constituent, SoS_Constituent.SoS_Constituent.constituent_id == Constituent.Constituent.constituent_id) \
        .filter(SoS.SoS.sos_id.in_((sos_list))).all()

        array_constituents = []

        for sos_id, relation_id, constituent_id in results:
            constituent = CS(constituent_id=constituent_id.constituent_id, constituent_name=constituent_id.constituent_name)
            array_constituents.append(constituent)
            #print(sos_id.sos_name, constituent_id.constituent_id, constituent_id.constituent_name)
            #print(array_constituents)
        return jsonify([e.toJSON() for e in array_constituents])
    except Exception as e:
	    return(str(e))           


    