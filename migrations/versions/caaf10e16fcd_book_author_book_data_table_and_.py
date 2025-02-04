"""book, author, book-data table and relations between them

Revision ID: caaf10e16fcd
Revises: 
Create Date: 2024-05-20 00:55:39.878514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caaf10e16fcd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('surname', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_author_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_author_surname'), ['surname'], unique=False)

    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_title'), ['title'], unique=True)

    op.create_table('book_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('rented', sa.Boolean(), nullable=True),
    sa.Column('rent_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book_data', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_data_rent_date'), ['rent_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_book_data_rented'), ['rented'], unique=False)

    op.create_table('books_authors',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'author_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books_authors')
    with op.batch_alter_table('book_data', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_data_rented'))
        batch_op.drop_index(batch_op.f('ix_book_data_rent_date'))

    op.drop_table('book_data')
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_title'))
        batch_op.drop_index(batch_op.f('ix_book_description'))

    op.drop_table('book')
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_author_surname'))
        batch_op.drop_index(batch_op.f('ix_author_name'))

    op.drop_table('author')
    # ### end Alembic commands ###
