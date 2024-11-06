"""Add Company.company_name_ko nullable option

Revision ID: cc9e6bbb1828
Revises: 98a9791bd3ba
Create Date: 2024-11-06 16:49:31.280952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'cc9e6bbb1828'
down_revision: Union[str, None] = '98a9791bd3ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('company', 'company_name_ko',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('company', 'company_name_ko',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)
    # ### end Alembic commands ###
