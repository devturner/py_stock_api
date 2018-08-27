from marshmallow_sqlalchemy import ModelSchema
# see the __init__ line 11 to make this work:

from . import Portfolio
from . import Stock


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio


class Stock(ModelSchema):
    class Meta:
        model = Stock
