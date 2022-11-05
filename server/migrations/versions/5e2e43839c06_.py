"""empty message

Revision ID: 5e2e43839c06
Revises: 
Create Date: 2022-11-05 12:45:55.371782

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5e2e43839c06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('basic_feature', sa.Column('feature_external_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column('emergent_behavior', sa.Column('emergent_external_id', postgresql.UUID(as_uuid=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('emergent_behavior', 'emergent_external_id')
    op.drop_column('basic_feature', 'feature_external_id')
    # ### end Alembic commands ###