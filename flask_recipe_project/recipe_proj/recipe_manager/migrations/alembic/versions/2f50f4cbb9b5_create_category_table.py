"""Create category table

Revision ID: 2f50f4cbb9b5
Revises: fef5cc5db307
Create Date: 2024-06-27 10:58:32.628497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f50f4cbb9b5'
down_revision: Union[str, None] = 'fef5cc5db307'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'category',
    sa.Column('category_id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(40), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('category')
