"""criar tabela atendimento

Revision ID: 0e8424471d84
Revises: 
Create Date: 2024-12-12 20:23:25.489092

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e8424471d84'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'atendimento',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('id_atendimento', sa.Integer, nullable=False),
        sa.Column('id_cliente', sa.Integer, nullable=False),
        sa.Column('angel', sa.String(length=255), nullable=False),
        sa.Column('polo', sa.String(length=255), nullable=False),
        sa.Column('data_limite', sa.Date, nullable=False),
        sa.Column('data_de_atendimento', sa.Date, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('atendimento')
