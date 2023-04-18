"""add foreign key to post_table

Revision ID: 49ab746c144a
Revises: 41fea6fff0d6
Create Date: 2023-04-17 12:12:48.446365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49ab746c144a'
down_revision = '41fea6fff0d6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table = 'posts', referent_table = 'users',
                            local_cols = ['user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name = 'posts')
    op.drop_column('posts', 'user_id')
    pass
