"""empty message

Revision ID: 02dc51621cc7
Revises: a12ea5615013
Create Date: 2018-01-15 23:22:30.186644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02dc51621cc7'
down_revision = 'a12ea5615013'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fightersToFights_fight_id_fkey', 'fightersToFights', type_='foreignkey')
    op.drop_constraint('fightersToFights_fighter_id_fkey', 'fightersToFights', type_='foreignkey')
    op.create_foreign_key(None, 'fightersToFights', 'fight', ['fight_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key(None, 'fightersToFights', 'fighter', ['fighter_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'fightersToFights', type_='foreignkey')
    op.drop_constraint(None, 'fightersToFights', type_='foreignkey')
    op.create_foreign_key('fightersToFights_fighter_id_fkey', 'fightersToFights', 'fighter', ['fighter_id'], ['id'])
    op.create_foreign_key('fightersToFights_fight_id_fkey', 'fightersToFights', 'fight', ['fight_id'], ['id'])
    # ### end Alembic commands ###
