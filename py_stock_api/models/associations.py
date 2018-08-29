from sqlalchemy import Table, Column, Integer, ForeignKey
from .meta import metadata


roles_association = Table(
    'roles_association',
    metadata,
    Column('account_id', Integer, ForeignKey('accounts.id')),
    Column('role_id', Integer, ForeignKey('account_roles.id'))
)

portfolios_associations = Table(
    'portfolio_association',
    metadata,
    Column('stock_id', Integer, ForeignKey('stocks.id')),
)
