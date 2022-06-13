"""add question

Revision ID: 394de6fdd3f2
Revises: d6d141cb435a
Create Date: 2022-05-18 10:27:05.000420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '394de6fdd3f2'
down_revision = 'd6d141cb435a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    # ### end Alembic commands ###