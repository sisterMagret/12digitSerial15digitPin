"""updates

Revision ID: 12c2b3cd743c
Revises: 6ffd0147fc42
Create Date: 2020-02-10 10:29:55.828737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12c2b3cd743c'
down_revision = '6ffd0147fc42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('s_No', sa.INTEGER(), nullable=False),
    sa.Column('pin', sa.VARCHAR(length=16), nullable=True),
    sa.PrimaryKeyConstraint('s_No'),
    sa.UniqueConstraint('pin'),
    sa.UniqueConstraint('s_No')
    )
    # ### end Alembic commands ###
