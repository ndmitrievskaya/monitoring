# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.dialects.postgresql import TEXT
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine(
#     "sqlite3://",
#     # "postgresql://postgres:postgres@postgres_db_container/url_monitoring",
#     echo=True)
# Base = declarative_base()
#
# make_session = sessionmaker(bind=engine)
#
#
# class Snapshots(Base):
#     __tablename__ = "url_monitoring_cache"
#
#     id = Column(Integer, primary_key=True)
#     timestamp = Column(String)
#     snapshot = Column(TEXT)

from gino.ext.starlette import Gino

from . import config

db = Gino(
    dsn=config.DB_DSN,
    echo=config.DB_ECHO,
)


class Snapshots(db.Model):
    __tablename__ = "snapshots"

    id = db.Column(db.BigInteger(), primary_key=True)
    timestamp = db.Column(db.DateTime())
    snapshot = db.Column(db.Unicode())
