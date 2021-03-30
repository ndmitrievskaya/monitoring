from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

DB_HOST = config("DB_HOST", default=None)
DB_PORT = config("DB_PORT", cast=int, default=None)
DB_USER = config("DB_USER", default=None)
DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default=None)
DB_DSN = "postgresql://postgres:postgres@localhost/snapshots"
DB_ECHO = True
