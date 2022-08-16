from app import db

class Basic_Feature(db.Model):
    __tablename__ = 'basic_feature'

    feature_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<feature_id {}>'.format(self.feature_id)
    
    def serialize(self):
        return {
            'feature_id': self.feature_id, 
            'description': self.description,
        }   