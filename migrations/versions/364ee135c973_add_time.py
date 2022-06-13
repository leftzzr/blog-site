"""add time

Revision ID: 364ee135c973
Revises: 958f0ba694c2
Create Date: 2022-05-18 14:06:13.415970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '364ee135c973'
down_revision = '958f0ba694c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'time')
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###