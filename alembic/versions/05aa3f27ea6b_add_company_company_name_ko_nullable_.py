"""Add Company.company_name_ko nullable option

Revision ID: 05aa3f27ea6b
Revises: a5f528333001
Create Date: 2024-11-06 23:44:32.546435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '05aa3f27ea6b'
down_revision: Union[str, None] = 'a5f528333001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('company', 'company_name_ko',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('company', 'company_name_ko',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)
    # ### end Alembic commands ###
