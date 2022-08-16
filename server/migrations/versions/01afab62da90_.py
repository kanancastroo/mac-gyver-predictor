"""empty message

Revision ID: 01afab62da90
Revises: 
Create Date: 2022-08-02 22:33:51.725121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01afab62da90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basic_feature',
    sa.Column('feature_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('feature_id')
    )
    op.create_table('constituent',
    sa.Column('constituent_id', sa.Integer(), nullable=False),
    sa.Column('constituent_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('constituent_id')
    )
    op.create_table('emergent_behavior',
    sa.Column('emergent_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('emergent_id')
    )
    op.create_table('sos',
    sa.Column('sos_id', sa.Integer(), nullable=False),
    sa.Column('sos_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('sos_id')
    )
    op.create_table('basic_feature_emergent_behavior',
    sa.Column('relation_id', sa.Integer(), nullable=False),
    sa.Column('basic_feature_id', sa.Integer(), nullable=True),
    sa.Column('emergent_behavior_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['basic_feature_id'], ['basic_feature.feature_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['emergent_behavior_id'], ['emergent_behavior.emergent_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('relation_id')
    )
    op.create_table('constituent_basic_feature',
    sa.Column('relation_id', sa.Integer(), nullable=False),
    sa.Column('basic_feature_id', sa.Integer(), nullable=True),
    sa.Column('constituent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['basic_feature_id'], ['basic_feature.feature_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['constituent_id'], ['constituent.constituent_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('relation_id')
    )
    op.create_table('constituent_sos',
    sa.Column('relation_id', sa.Integer(), nullable=False),
    sa.Column('sos_id', sa.Integer(), nullable=True),
    sa.Column('constituent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['constituent_id'], ['constituent.constituent_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sos_id'], ['sos.sos_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('relation_id')
    )
    op.create_table('sos_emergent_behavior',
    sa.Column('relation_id', sa.Integer(), nullable=False),
    sa.Column('sos_id', sa.Integer(), nullable=True),
    sa.Column('emergent_behavior_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['emergent_behavior_id'], ['emergent_behavior.emergent_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['sos_id'], ['sos.sos_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('relation_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sos_emergent_behavior')
    op.drop_table('constituent_sos')
    op.drop_table('constituent_basic_feature')
    op.drop_table('basic_feature_emergent_behavior')
    op.drop_table('sos')
    op.drop_table('emergent_behavior')
    op.drop_table('constituent')
    op.drop_table('basic_feature')
    # ### end Alembic commands ###
