"""Users, Videos with \relationships

Revision ID: e681f1ada7ff
Revises: 
Create Date: 2022-04-28 16:24:42.047916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e681f1ada7ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('creator', 'manager', 'admin', name='user_type_enum'), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('profile_picture_link', sa.String(), nullable=True),
    sa.Column('cover_picture_link', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('cv_link', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_users_type'), ['type'], unique=False)
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    op.create_table('videos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('videos', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_videos_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('videos', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_videos_id'))

    op.drop_table('videos')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.drop_index(batch_op.f('ix_users_type'))
        batch_op.drop_index(batch_op.f('ix_users_id'))

    op.drop_table('users')
    # ### end Alembic commands ###