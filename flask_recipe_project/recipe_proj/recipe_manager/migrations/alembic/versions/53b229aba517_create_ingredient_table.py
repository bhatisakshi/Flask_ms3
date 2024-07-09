"""Create ingredient table

Revision ID: 53b229aba517
Revises: 2f50f4cbb9b5
Create Date: 2024-06-27 11:02:16.202686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53b229aba517'
down_revision: Union[str, None] = '2f50f4cbb9b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'ingredient',
    sa.Column('ingredient_id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(40), nullable=False),
    sa.Column('quantity', sa.Integer, nullable=False)
)

def downgrade() -> None:
    op.drop_table('ingredient')
