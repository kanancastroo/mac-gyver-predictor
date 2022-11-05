from app import db
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

class Basic_Feature(db.Model):
    __tablename__ = 'basic_feature'

    feature_id = db.Column(db.Integer, primary_key=True)
    feature_external_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    description = db.Column(db.String())

    def __init__(self, feature_external_id, description):
        self.description = description
        self.feature_external_id = feature_external_id

    def __repr__(self):
        return '<feature_external_id {}>'.format(self.feature_external_id)
    
    def serialize(self):
        return {
            'feature_external_id': self.feature_external_id, 
            'description': self.description,
        }   