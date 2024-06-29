"""add unique scene key

Revision ID: 0102ff341fb3
Revises: 1a878c24a969
Create Date: 2024-06-25 15:46:54.563526

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0102ff341fb3'
down_revision: Union[str, None] = '1a878c24a969'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dim_scene', sa.Column('SceneKey', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dim_scene', 'SceneKey')
    # ### end Alembic commands ###