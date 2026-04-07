"""merge multiple heads

Revision ID: 71893cb05099
Revises: 2f656db09c83, fb7c20665d76
Create Date: 2026-04-07 10:12:21.800703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71893cb05099'
down_revision = ('2f656db09c83', 'fb7c20665d76')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
