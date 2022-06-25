"""empty message

Revision ID: 66099a520da4
Revises: 
Create Date: 2022-06-25 19:05:01.213772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66099a520da4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sos')
    # ### end Alembic commands ###
