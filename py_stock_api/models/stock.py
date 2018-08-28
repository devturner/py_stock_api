from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


class Stock(Base):
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

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())


@classmethod
def new(cls, request, **kwargs):
    if request.dbsessiom is None:
        raise DBAPIError
    stock = cls(**kwargs)
    request.dbsession.add(stock)

    return request.dbsession.query(cls).filter(
        cls.symbol == kwargs['symbol']).one_or_none()

# @classmethod
# def all(cls, request):
#     if request.dbsessiom is None:
#         raise DBAPIError

#     return request.debsessions.query(cls).all()

@classmethod
def one(cls, request, pk=None):
    if request.dbsessiom is None:
        raise DBAPIError

    return request.debsessions.query(cls).get(pk)

@classmethod
def destroy(cls, request=None, pk=None):
    if request.dbsessiom is None:
        raise DBAPIError

    return request.debsessions.query(cls).get(pk).delete()

