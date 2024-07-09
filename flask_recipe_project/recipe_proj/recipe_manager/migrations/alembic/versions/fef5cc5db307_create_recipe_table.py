"""create recipe table

Revision ID: fef5cc5db307
Revises: 
Create Date: 2024-06-27 10:44:33.962154

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fef5cc5db307'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'recipe', 
    sa.Column('recipe_id',sa.Integer, primary_key=True),
    sa.Column('title', sa.String(100)),
    sa.Column('description', sa.String(300), nullable=False),
    sa.Column('preparation_time', sa.Integer, nullable=False),
    sa.Column('instructions', sa.String(500), nullable=False),
)

def downgrade() -> None:
    op.drop_table('recipe')