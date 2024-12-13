"""criar tabela usuario

Revision ID: 4a870803f55b
Revises: 0e8424471d84
Create Date: 2024-12-12 21:13:53.353979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a870803f55b'
down_revision: Union[str, None] = '0e8424471d84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'usuario',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False, unique=True),
        sa.Column('senha', sa.String(length=255), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('usuario')
