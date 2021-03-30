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
