from app import db

class Constituent(db.Model):
    __tablename__ = 'constituent'

    constituent_id = db.Column(db.Integer, primary_key=True)
    constituent_name = db.Column(db.String())

    def __init__(self, constituent_name):
        self.constituent_name = constituent_name

    def __repr__(self):
        return '<constituent_id {}>'.format(self.constituent_id)
    
    def serialize(self):
        return {
            'constituent_id': self.constituent_id, 
            'constituent_name': self.constituent_name,
        }    