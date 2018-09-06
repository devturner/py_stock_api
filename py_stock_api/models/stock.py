from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)

from .meta import Base


class Stock(Base):
    """ building the stock table in the database
    """
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    companyName = Column(Text)
    exchange = Column(Text)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    CEO = Column(Text)
    issueType = Column(Text)
    sector = Column(Text)

    portfolios = relationship('Portfolio', back_populates='stocks')
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'), nullable=False)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())


    @classmethod
    def new(cls, request, **kwargs):
        """ Add a new stock to the a db
        """
        if request.dbsession is None:
            raise DBAPIError
        stock = cls(**kwargs)
        request.dbsession.add(stock)

        return request.dbsession.query(cls).filter(
            cls.symbol == kwargs['symbol']).one_or_none()

    # @classmethod
    # def all(cls, request):
    #     if request.dbsession is None:
    #         raise DBAPIError

    #     return request.dbsession.query(cls).all()

    @classmethod
    def one(cls, request, pk=None):
        """ get one stock from the database
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def destroy(cls, request=None, pk=None):
        """ Delete a stock record from the database
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk).delete()

