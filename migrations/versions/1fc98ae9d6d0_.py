"""empty message

Revision ID: 1fc98ae9d6d0
Revises: 404502460c90
Create Date: 2024-11-02 23:28:22.065125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1fc98ae9d6d0'
down_revision: Union[str, None] = '404502460c90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
