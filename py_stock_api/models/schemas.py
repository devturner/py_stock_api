from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio
from . import Stock
from . import AccountRole
from . import Account


class PortfolioSchema(ModelSchema):
    """ Portfolio Schema for the db
    """
    class Meta:
        model = Portfolio


class StockSchema(ModelSchema):
    """ Stock Schema for the db
    """
    class Meta:
        model = Stock


class AccountRoleSchema(ModelSchema):
    """ Account Role Schema for the db
    """
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    """ Account Schema for the db
    """
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account
