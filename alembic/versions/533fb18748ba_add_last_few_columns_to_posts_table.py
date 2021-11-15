"""add last few columns to posts table

Revision ID: 533fb18748ba
Revises: d49403e9a37f
Create Date: 2021-11-15 11:46:27.621536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '533fb18748ba'
down_revision = 'd49403e9a37f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(),
                  nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text("NOW()")))
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
