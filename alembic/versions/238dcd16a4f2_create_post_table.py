"""create post table

Revision ID: 238dcd16a4f2
Revises: 
Create Date: 2023-04-17 11:07:59.095692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '238dcd16a4f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
                    sa.Column('title', sa.String(), nullable = False),
                    sa.Column('content', sa.String(), nullable = False),
                    )

    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
