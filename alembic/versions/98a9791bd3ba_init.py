"""Init

Revision ID: 98a9791bd3ba
Revises: 
Create Date: 2024-11-06 16:47:49.368158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98a9791bd3ba'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name_ko', sa.String(length=256), nullable=True),
    sa.Column('company_name_en', sa.String(length=256), nullable=True),
    sa.Column('company_name_ja', sa.String(length=256), nullable=True),
    sa.Column('company_tag_ko', sa.Text(), nullable=True),
    sa.Column('company_tag_en', sa.Text(), nullable=True),
    sa.Column('company_tag_ja', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    # ### end Alembic commands ###
