"""Create recipeingredient table

Revision ID: 66530bf1b8e3
Revises: 53b229aba517
Create Date: 2024-06-27 11:19:38.452407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66530bf1b8e3'
down_revision: Union[str, None] = '53b229aba517'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'recipeingredient',
    sa.Column('recipeingredient_id', sa.Integer, primary_key=True),
    sa.Column('recipe', sa.String, sa.ForeignKey('recipe.title')),
    sa.Column('ingredient', sa.String, sa.ForeignKey('ingredient.name')),
    sa.Column('quantity', sa.Integer)
)

def downgrade():
    op.drop_table('recipeingredient')
