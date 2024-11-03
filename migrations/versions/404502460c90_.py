"""empty message

Revision ID: 404502460c90
Revises: 43e55534ac55
Create Date: 2024-11-02 23:03:02.597546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '404502460c90'
down_revision: Union[str, None] = '43e55534ac55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
