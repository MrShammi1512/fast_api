from sqlalchemy import MetaData
from databases import Database

db_rul= "mysql+asyncmy://root:root@localhost:3306/productdb"

database= Database(db_rul)
metadata= MetaData()