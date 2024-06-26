"""rename Scene_ID to SceneID in fact_backtests table

Revision ID: 58cdc5f2d9f3
Revises: 385ed44b1e0c
Create Date: 2024-06-25 21:30:29.839809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58cdc5f2d9f3'
down_revision: Union[str, None] = '385ed44b1e0c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fact_backtests', sa.Column('SceneID', sa.Integer(), nullable=True))
    op.drop_constraint('fact_backtests_Scene_ID_fkey', 'fact_backtests', type_='foreignkey')
    op.create_foreign_key(None, 'fact_backtests', 'dim_scene', ['SceneID'], ['SceneID'])
    op.drop_column('fact_backtests', 'Scene_ID')
    op.create_foreign_key(None, 'fact_trades', 'dim_strategy', ['StrategyID'], ['StrategyID'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'fact_trades', type_='foreignkey')
    op.add_column('fact_backtests', sa.Column('Scene_ID', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'fact_backtests', type_='foreignkey')
    op.create_foreign_key('fact_backtests_Scene_ID_fkey', 'fact_backtests', 'dim_scene', ['Scene_ID'], ['SceneID'])
    op.drop_column('fact_backtests', 'SceneID')
    # ### end Alembic commands ###
