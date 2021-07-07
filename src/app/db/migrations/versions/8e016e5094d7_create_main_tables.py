"""create_main_tables

Revision ID: 8e016e5094d7
Revises: 
Create Date: 2021-07-02 21:38:05.020288

"""
from sqlalchemy.sql.expression import false
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '8e016e5094d7'
down_revision = None
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

