from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, BigInteger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "usesrs"
    id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    prime = Column(Boolean, nullable=False, default=False)
    data = Column(JSONB, default={})


class Tarot_Reader(Base):
    __tablename__ = "tarot_reader"
    id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    ended_orders = Column(Integer, nullable=False, default=0)
    price = Column(Integer, nullable=False, default=0)
    paid_amount = Column(Integer, nullable=False, default=0)
    debt = Column(Integer, default=0)
    statistic = Column(Float, default=100.0)


class Horoscopes(Base):
    __tablename__ = "horoscopes"
    id = Column(
        BigInteger,
        primary_key=True,
        unique=True,
    )
    sign = Column(
        String,
        nullable=False,
    )
    theme = Column(String, nullable=False)
    type = Column(String, nullable=False)
    text = Column(String, nullable=False)
    date_of_update = Column(String, nullable=False)
