""""last_protection_state"

Revision ID: cc36af074e8a
Revises: 99c21687e80a
Create Date: 2018-04-27 11:40:00.384991

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cc36af074e8a'
down_revision = '99c21687e80a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('device_state',
                  sa.Column('last_protection_state', sa.Enum(
                      'unprotected', 'protected', 'parked',
                      'error', 'replicating', 'warned'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('device_state', 'last_protection_state')
    # ### end Alembic commands ###