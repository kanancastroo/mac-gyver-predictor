from app import db
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

class Constituent(db.Model):
    __tablename__ = 'constituent'

    constituent_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    constituent_external_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    constituent_name = db.Column(db.String())

    def __init__(self, constituent_external_id, constituent_name):
        self.constituent_name = constituent_name
        self.constituent_external_id = constituent_external_id

    def __repr__(self):
        return '<constituent_external_id {}>'.format(self.constituent_external_id)
    
    def serialize(self):
        return {
            'constituent_external_id': self.constituent_external_id, 
            'constituent_name': self.constituent_name,
        }    