"""Create recipecategory table

Revision ID: e83530449b13
Revises: 66530bf1b8e3
Create Date: 2024-06-27 11:19:48.813564

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e83530449b13'
down_revision: Union[str, None] = '66530bf1b8e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'recipecategory',
    sa.Column('recipecategory_id ', sa.Integer, primary_key=True),
    sa.Column('recipe', sa.String, sa.ForeignKey('recipe.title')),
    sa.Column('category', sa.String, sa.ForeignKey('category.name'))
)

def downgrade():
    op.drop_table('recipecategory')
