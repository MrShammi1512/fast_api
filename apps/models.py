from sqlalchemy import Column, Integer, String, Table, MetaData
from database import metadata
from pydantic import BaseModel

product =Table(
    "product",
    metadata,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("name",String(100), nullable=False),
    Column("price", Integer, nullable=False)
)

class ProductIn(BaseModel):
    name: str
    price : float

class ProductOut(ProductIn):
    id : int