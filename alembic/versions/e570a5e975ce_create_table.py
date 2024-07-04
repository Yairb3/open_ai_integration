"""Create table

Revision ID: e570a5e975ce
Revises: 
Create Date: 2024-07-04 22:17:53.800657

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e570a5e975ce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "questions_and_answers",
        sa.Column("id", sa.Integer, primary_key=True ),
        sa.Column("question", sa.String, nullable=False ),
        sa.Column("answer", sa.String, nullable=False )
    )


def downgrade() -> None:
    op.drop_table()
