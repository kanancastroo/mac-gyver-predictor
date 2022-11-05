from app import app, db
from flask import jsonify, request
from models import SoS, SoS_Constituent, Constituent
from sqlalchemy import update
import jsons
import numpy as np
import array as arr
import uuid

@app.route("/sos/get")
def getAllSoS():
    try:
        sos=SoS.SoS.query.all()
        return  jsonify([e.serialize() for e in sos])
    except Exception as e:
	    return(str(e))   

@app.route("/sos/add")
def addSoS():
    sos_name=request.args.get('sos_name')
    try:
        sos=SoS.SoS(
            sos_external_id = uuid.uuid4().hex,
            sos_name = sos_name
        )
        db.session.add(sos)
        db.session.commit()
        return "SoS added. sos_external_id={}.".format(sos.sos_external_id)
    except Exception as e:
	    return(str(e))  

@app.route("/sos/<sos_id>/get")
def getSoS(sos_id):
    sos_external_id=str(sos_id)
    try:
        sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).first()
        return jsonify(sos.sos_name)
    except Exception as e:
	    return(str(e))                

@app.route("/sos/<sos_id>/update")
def updateSoS(sos_id):
    sos_external_id=str(sos_id)
    sos_name=request.args.get('sos_name')
    try:
        sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).first()
        sos.sos_name = sos_name
        db.session.commit()
        return "SoS updated. sos_external_id={}.".format(sos.sos_external_id)
    except Exception as e:
	    return(str(e))                       

@app.route("/sos/<sos_id>/delete")
def deleteSoS(sos_id):
    sos_external_id=str(sos_id)
    try:
        sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).one()
        db.session.delete(sos)
        db.session.commit()
        return "SoS id={} was deleted sucessfully.".format(sos_external_id)
    except Exception as e:
	    return(str(e))       


@app.route("/sos/<sos_id>/constituents/get")
def getConstituentsFromSoS(sos_id):
    class CS():
        def __init__(self, constituent_external_id, constituent_name):
            # self.constituent_id = constituent_id
            self.constituent_external_id = constituent_external_id
            self.constituent_name = constituent_name

        def toJSON(self):
            return jsons.dump(self)

    sos_external_id=str(sos_id)
    sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).one()

    sos_id=sos.sos_id
    # print('internal ID iS =>>> ', sos_id)
    # aux = sos_id[1:-1]
    # arr = aux.split(sep=',')
    # print(arr)
    # sos_list = np.array(arr)
    # for i in range(len(test)):
    #     print(i, ' IS => ', test[i])
    # test = arr.array('i', test1)
    # print(test)
    try:
        results = db.session.query(SoS.SoS, SoS_Constituent.SoS_Constituent, Constituent.Constituent) \
        .select_from(SoS.SoS) \
        .join(SoS_Constituent.SoS_Constituent, SoS.SoS.sos_id == SoS_Constituent.SoS_Constituent.sos_id) \
        .join(Constituent.Constituent, SoS_Constituent.SoS_Constituent.constituent_id == Constituent.Constituent.constituent_id) \
        .filter(SoS.SoS.sos_id == sos_id).all()
        # .filter(SoS.SoS.sos_id.in_((sos_list))).all()

        array_constituents = []

        for sos_id, relation_id, constituent_id in results:
            constituent = CS(constituent_external_id=constituent_id.constituent_external_id, constituent_name=constituent_id.constituent_name)
            array_constituents.append(constituent)
            #print(sos_id.sos_name, constituent_id.constituent_id, constituent_id.constituent_name)
            #print(array_constituents)
        return jsonify([e.toJSON() for e in array_constituents])
    except Exception as e:
	    return(str(e))           


    