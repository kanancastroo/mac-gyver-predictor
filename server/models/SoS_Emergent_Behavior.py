from app import db

class SoS_Emergent_Behavior(db.Model):
    __tablename__ = 'sos_emergent_behavior'

    relation_id = db.Column(db.Integer, primary_key=True)
    sos_id = db.Column(db.Integer, db.ForeignKey("sos.sos_id", ondelete="CASCADE"))
    emergent_behavior_id  = db.Column(db.Integer, db.ForeignKey("emergent_behavior.emergent_id", ondelete="CASCADE"))

    def __init__(self, sos_id, emergent_behavior_id):
        self.sos_id = sos_id
        self.emergent_behavior_id = emergent_behavior_id

    def __repr__(self):
        return '<relation_id {}>'.format(self.relation_id)
    
    def serialize(self):
        return {
            'relation_id': self.relation_id, 
            'sos_id': self.sos_id,
            'emergent_behavior_id': self.emergent_behavior_id,
        }    