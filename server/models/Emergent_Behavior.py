from app import db
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

class Emergent_Behavior(db.Model):
    __tablename__ = 'emergent_behavior'

    emergent_id = db.Column(db.Integer, primary_key=True)
    emergent_external_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    description = db.Column(db.String())

    def __init__(self, emergent_external_id, description):
        self.emergent_external_id = emergent_external_id
        self.description = description

    def __repr__(self):
        return '<emergent_external_id {}>'.format(self.emergent_external_id)
    
    def serialize(self):
        return {
            'emergent_external_id': self.emergent_external_id, 
            'description': self.description,
        }  