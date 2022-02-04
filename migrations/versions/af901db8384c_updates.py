"""updates

Revision ID: af901db8384c
Revises: 13d06277e715
Create Date: 2022-02-04 00:24:26.769652

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'af901db8384c'
down_revision = '13d06277e715'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reviews')
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('movie_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('image_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('movie_review', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='reviews_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    op.drop_table('profile_photos')
    # ### end Alembic commands ###