from app import db

class Basic_Feature_Emergent_Behavior(db.Model):
    __tablename__ = 'basic_feature_emergent_behavior'

    relation_id = db.Column(db.Integer, primary_key=True)
    basic_feature_id = db.Column(db.Integer, db.ForeignKey("basic_feature.feature_id", ondelete="CASCADE"))
    emergent_behavior_id  = db.Column(db.Integer, db.ForeignKey("emergent_behavior.emergent_id", ondelete="CASCADE"))

    def __init__(self, basic_feature_id, emergent_behavior_id):
        self.basic_feature_id = basic_feature_id
        self.emergent_behavior_id = emergent_behavior_id

    def __repr__(self):
        return '<relation_id {}>'.format(self.relation_id)
    
    def serialize(self):
        return {
            'relation_id': self.relation_id, 
            'basic_feature_id': self.basic_feature_id,
            'emergent_behavior_id': self.emergent_behavior_id,
        }  