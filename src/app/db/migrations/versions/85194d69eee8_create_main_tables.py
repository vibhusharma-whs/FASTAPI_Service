"""create_main_tables

Revision ID: 85194d69eee8
Revises: 8e016e5094d7
Create Date: 2021-07-07 03:08:18.700286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '85194d69eee8'
down_revision = '8e016e5094d7'
branch_labels = None
depends_on = None

def create_finding_table() -> None:
    op.create_table(
        "finding",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("finding_class_id", sa.Integer, nullable=False),
        sa.Column("application_id", sa.Integer, nullable=False),
        sa.Column("uri", sa.Text, nullable=False),
        sa.Column("signature", sa.Text, nullable=False, server_default="example_signature"),
        sa.Column("state", sa.Integer),
        sa.Column("create_time", sa.TIMESTAMP),
        sa.Column("update_time", sa.TIMESTAMP),
    )

def upgrade() -> None:
    create_finding_table()
    
def downgrade() -> None:
    op.drop_table("finding")
