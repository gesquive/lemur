"""Adding ability to mark domains as 'sensitive'

Revision ID: 4c50b903d1ae
Revises: 33de094da890
Create Date: 2015-12-30 10:19:30.057791

"""

# revision identifiers, used by Alembic.
revision = '4c50b903d1ae'
down_revision = '33de094da890'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('domains', sa.Column('sensitive', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('domains', 'sensitive')
    ### end Alembic commands ###
