import sqlalchemy as sa
from databases import Database

from src.config import DATABASE_URL

engine = sa.create_engine(DATABASE_URL)
metadata = sa.MetaData()
database = Database(DATABASE_URL)

example = sa.Table(
    "example",
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String),
)

metadata.create_all(engine)