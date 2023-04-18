"""users table

Revision ID: 41fea6fff0d6
Revises: 238dcd16a4f2
Create Date: 2023-04-17 11:52:37.553355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41fea6fff0d6'
down_revision = '238dcd16a4f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
