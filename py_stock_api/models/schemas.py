# TODO come back to this in vids (it'll be near the end)

from marshmallow_sqlalchemy import ModelSchema
# see the __init__ line 11 to make this work:
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio
from . import Stock
from . import AccountRole
from . import Account
# from . import Stock


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio


class StockSchema(ModelSchema):
    class Meta:
        model = Stock


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account
