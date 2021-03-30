"""Create snapshots table

Revision ID: d70e105f323c
Revises: 
Create Date: 2021-03-30 10:53:07.571194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd70e105f323c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('snapshots',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('snapshot', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('snapshots')
    # ### end Alembic commands ###
