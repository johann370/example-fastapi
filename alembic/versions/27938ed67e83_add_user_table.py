"""add user table

Revision ID: 27938ed67e83
Revises: 9879b56e777a
Create Date: 2021-11-15 11:38:01.141185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27938ed67e83'
down_revision = '9879b56e777a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
