from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from .stock import Stock
from .meta import Base
# from .associations import portfolios_associations
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)


class Portfolio(Base):
    """ Create the portfolios table
    """
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    stocks = relationship('Stock', back_populates='portfolios')
    accounts = relationship('Account', back_populates='portfolios')
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())


    @classmethod
    def new(cls, request, **kwargs):
        """ Create a new portfolio
        """
        if request.dbsession is None:
            raise DBAPIError
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.name == kwargs['name']).one_or_none()

    @classmethod
    def all(cls, request):
        """List all the portfolios
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()

    @classmethod
    def one(cls, request, pk=None):
        """List one of the portfolios
        """
        if request.dbsession is None:
            raise DBAPIError
        import pdb; pdb.set_trace()
        return request.dbsession.query(cls).get(pk)

    @classmethod
    def destroy(cls, request=None, pk=None):
        """delete a portfolio
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk).delete()

