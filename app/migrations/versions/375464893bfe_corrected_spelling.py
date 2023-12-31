"""corrected spelling

Revision ID: 375464893bfe
Revises: a628f61ed6e8
Create Date: 2023-06-27 09:08:08.902916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '375464893bfe'
down_revision = 'a628f61ed6e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(), nullable=True),
    sa.Column('application_date', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('job-applications')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job-applications',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('job_title', sa.VARCHAR(), nullable=True),
    sa.Column('application_date', sa.VARCHAR(), nullable=True),
    sa.Column('status', sa.VARCHAR(), nullable=True),
    sa.Column('notes', sa.VARCHAR(), nullable=True),
    sa.Column('company_id', sa.INTEGER(), nullable=True),
    sa.Column('contact_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('job_applications')
    # ### end Alembic commands ###
