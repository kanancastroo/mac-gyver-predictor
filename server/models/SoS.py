from app import db

class SoS(db.Model):
    __tablename__ = 'sos'

    sos_id = db.Column(db.Integer, primary_key=True)
    sos_name = db.Column(db.String())

    def __init__(self, sos_name):
        self.sos_name = sos_name

    def __repr__(self):
        return '<sos_id {}>'.format(self.sos_id)
    
    def serialize(self):
        return {
            'sos_id': self.sos_id, 
            'sos_name': self.sos_name,
        }    