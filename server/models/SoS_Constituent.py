from app import db

class SoS_Constituent(db.Model):
    __tablename__ = 'constituent_sos'

    relation_id = db.Column(db.Integer, primary_key=True)
    sos_id = db.Column(db.Integer, db.ForeignKey("sos.sos_id", ondelete="CASCADE"))
    constituent_id = db.Column(db.Integer, db.ForeignKey("constituent.constituent_id", ondelete="CASCADE"))

    def __init__(self, sos_id, constituent_id):
        self.sos_id = sos_id
        self.constituent_id = constituent_id

    def __repr__(self):
        return '<relation_id {}>'.format(self.relation_id)
    
    def serialize(self):
        return {
            'relation_id': self.relation_id, 
            'sos_id': self.sos_id,
            'constituent_id': self.constituent_id,
        }    