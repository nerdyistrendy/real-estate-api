"""empty message

Revision ID: 0f82a9aaafa1
Revises: 82e1c5776417
Create Date: 2019-08-25 16:57:22.294484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0f82a9aaafa1"
down_revision = "82e1c5776417"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "locations", "neighbourhood", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column("locations", "street", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("locations", "street", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column(
        "locations", "neighbourhood", existing_type=sa.VARCHAR(), nullable=False
    )
    # ### end Alembic commands ###
