"""Add washing_machines table

Revision ID: 164f22a82d8c
Revises: 
Create Date: 2024-12-06 12:06:58.278357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '164f22a82d8c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('washing_machines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('installation_date', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('balance', sa.Float(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_washing_machines_id'), 'washing_machines', ['id'], unique=False)
    op.create_index(op.f('ix_washing_machines_name'), 'washing_machines', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_washing_machines_name'), table_name='washing_machines')
    op.drop_index(op.f('ix_washing_machines_id'), table_name='washing_machines')
    op.drop_table('washing_machines')
    # ### end Alembic commands ###