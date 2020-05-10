"""speed

Revision ID: d29e3791ac96
Revises: 3d8514d11619
Create Date: 2020-04-30 18:53:32.466964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd29e3791ac96'
down_revision = '3d8514d11619'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('speed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'speed')
    # ### end Alembic commands ###