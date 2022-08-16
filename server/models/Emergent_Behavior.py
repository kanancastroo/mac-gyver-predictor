from app import db

class Emergent_Behavior(db.Model):
    __tablename__ = 'emergent_behavior'

    emergent_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<emergent_id {}>'.format(self.emergent_id)
    
    def serialize(self):
        return {
            'emergent_id': self.emergent_id, 
            'description': self.description,
        }  