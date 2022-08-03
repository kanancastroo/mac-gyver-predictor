from app import db

class Constituent_Basic_Feature(db.Model):
    __tablename__ = 'constituent_basic_feature'

    relation_id = db.Column(db.Integer, primary_key=True)
    basic_feature_id = db.Column(db.Integer, db.ForeignKey("basic_feature.feature_id", ondelete="CASCADE"))
    constituent_id = db.Column(db.Integer, db.ForeignKey("constituent.constituent_id", ondelete="CASCADE"))

    def __init__(self, basic_feature_id, constituent_id):
        self.basic_feature_id = basic_feature_id
        self.constituent_id = constituent_id

    def __repr__(self):
        return '<relation_id {}>'.format(self.relation_id)
    
    def serialize(self):
        return {
            'relation_id': self.relation_id, 
            'basic_feature_id': self.basic_feature_id,
            'constituent_id': self.constituent_id,
        }  