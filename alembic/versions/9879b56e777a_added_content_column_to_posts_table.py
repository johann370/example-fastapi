"""added content column to posts table

Revision ID: 9879b56e777a
Revises: a587c5e54d7c
Create Date: 2021-11-15 11:35:12.941067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9879b56e777a'
down_revision = 'a587c5e54d7c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
