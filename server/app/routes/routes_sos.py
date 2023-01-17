from app import app, db
from flask import jsonify, request, Response
from models import SoS, SoS_Constituent, Constituent, Constituent_Basic_Feature, Basic_Feature, SoS_Emergent_Behavior, Emergent_Behavior
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
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )   

@app.route("/sos/add")
def addSoS():
    sos_name=request.args.get('sos_name')
    sos_external_id=request.args.get('sos_id')
    try:
        sos=SoS.SoS(
            sos_external_id = sos_external_id,
            sos_name = sos_name
        )
        db.session.add(sos)
        db.session.commit()
        return "SoS added. sos_external_id={}.".format(sos.sos_external_id)
    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )  

@app.route("/sos/<sos_id>/get")
def getSoS(sos_id):
    sos_external_id=str(sos_id)
    try:
        sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).first()
        return jsonify(sos.sos_name)
    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )                

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
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )                       

@app.route("/sos/<sos_id>/delete")
def deleteSoS(sos_id):
    sos_external_id=str(sos_id)
    try:
        sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).one()
        db.session.delete(sos)
        db.session.commit()
        return "SoS id={} was deleted sucessfully.".format(sos_external_id)
    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )       


@app.route("/sos/<sos_external_id>/constituents/get")
def getConstituentsFromSoS(sos_external_id):
    class CS():
        def __init__(self, constituent_external_id, constituent_name):
            # self.constituent_id = constituent_id
            self.constituent_external_id = constituent_external_id
            self.constituent_name = constituent_name

        def toJSON(self):
            return jsons.dump(self)

    sos_external_id=str(sos_external_id)
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
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )           


@app.route("/sos/<sos_external_id>/constituents/basic_features/get")
def getBasicFeaturesFromSoS(sos_external_id):
    class BasicFeature():
        def __init__(self, feature_external_id, description):
            # self.constituent_id = constituent_id
            self.feature_external_id = feature_external_id
            self.description = description

        def toJSON(self):
            return jsons.dump(self)

    sos_external_id=str(sos_external_id)
    sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).one()

    sos_id=sos.sos_id

    try:
        results = db.session.query(SoS.SoS, SoS_Constituent.SoS_Constituent, Constituent.Constituent, Constituent_Basic_Feature.Constituent_Basic_Feature, Basic_Feature.Basic_Feature) \
        .select_from(SoS.SoS) \
        .join(SoS_Constituent.SoS_Constituent, SoS.SoS.sos_id == SoS_Constituent.SoS_Constituent.sos_id) \
        .join(Constituent.Constituent, SoS_Constituent.SoS_Constituent.constituent_id == Constituent.Constituent.constituent_id) \
        .join(Constituent_Basic_Feature.Constituent_Basic_Feature, Constituent.Constituent.constituent_id == Constituent_Basic_Feature.Constituent_Basic_Feature.constituent_id) \
        .join(Basic_Feature.Basic_Feature, Constituent_Basic_Feature.Constituent_Basic_Feature.basic_feature_id == Basic_Feature.Basic_Feature.feature_id) \
        .filter(SoS.SoS.sos_id == sos_id).all()
        # .filter(SoS.SoS.sos_id.in_((sos_list))).all()

        array_basic_features = []

        for sos_id, sos_constituent, constituent_id, constituent_basic_feature, feature_id in results:
            basic_feature = BasicFeature(feature_external_id=feature_id.feature_external_id, description=feature_id.description)
            array_basic_features.append(basic_feature)
            # print(sos_id.sos_name, constituent_id.constituent_name, feature_id.description)
            #print(array_constituents)

        # print(array_basic_features)

        seen_ids = set()
        new_list = []
        for obj in array_basic_features:
            if obj.feature_external_id not in seen_ids:
                new_list.append(obj)
                seen_ids.add(obj.feature_external_id)

        return jsonify([e.toJSON() for e in new_list])
    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )      


@app.route("/sos/<sos_external_id>/constituents/basic_features/emergent_behaviors/get")
def getEmergentBehaviorsFromSoS(sos_external_id):
    class EmergentBehavior():
        def __init__(self, emergent_external_id, description):
            # self.constituent_id = constituent_id
            self.emergent_external_id = emergent_external_id
            self.description = description

        def toJSON(self):
            return jsons.dump(self)

    sos_external_id=str(sos_external_id)
    sos = SoS.SoS.query.filter_by(sos_external_id=sos_external_id).one()

    sos_id=sos.sos_id

    try:
        results = db.session.query(SoS.SoS, SoS_Emergent_Behavior.SoS_Emergent_Behavior, Emergent_Behavior.Emergent_Behavior) \
        .select_from(SoS.SoS) \
        .join(SoS_Emergent_Behavior.SoS_Emergent_Behavior, SoS.SoS.sos_id == SoS_Emergent_Behavior.SoS_Emergent_Behavior.sos_id) \
        .join(Emergent_Behavior.Emergent_Behavior, SoS_Emergent_Behavior.SoS_Emergent_Behavior.emergent_behavior_id == Emergent_Behavior.Emergent_Behavior.emergent_id) \
        .filter(SoS.SoS.sos_id == sos_id).all()
        # .filter(SoS.SoS.sos_id.in_((sos_list))).all()

        array_emergent_behaviors = []

        for sos, sos_emergent_behavior, emergent in results:
            emergent_behavior = EmergentBehavior(emergent_external_id=emergent.emergent_external_id, description=emergent.description)
            array_emergent_behaviors.append(emergent_behavior)
            # print(sos_id.sos_name, constituent_id.constituent_name, feature_id.description)
            #print(array_constituents)

        # print(array_basic_features)

        # TRECHO ABAIXO ESTÁ COM ERRO, NECESSÁRIO REVISAR. MAS TALVEZ NEM PRECISE DELE
        # seen_ids = set()
        # new_list = []
        # for obj in array_basic_features:
        #     if obj.feature_id not in seen_ids:
        #         new_list.append(obj)
        #         seen_ids.add(obj.feature_id)

        return jsonify([e.toJSON() for e in array_emergent_behaviors])
    except Exception as e:
	    return Response(
                "Internal Server Error {}".format(e),
                status=500,
            )      