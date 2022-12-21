from app import db
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

class SoS(db.Model):
    __tablename__ = 'sos'

    sos_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sos_external_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    sos_name = db.Column(db.String())

    def __init__(self, sos_external_id, sos_name):
        self.sos_name = sos_name
        self.sos_external_id = sos_external_id

    def __repr__(self):
        return '<sos_external_id {}>'.format(self.sos_external_id)
    
    def serialize(self):
        return {
            'sos_external_id': self.sos_external_id, 
            'sos_name': self.sos_name,
        }    