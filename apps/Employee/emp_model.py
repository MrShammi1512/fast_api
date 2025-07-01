from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Table, MetaData
from apps.database import database,metadata



employee =Table(
    "employee",
    metadata,
Column("emp_id",Integer,primary_key=True, autoincrement=True),
Column("emp_name",String,nullable=False),
Column("emp_age",Integer,nullable=False),
Column("emp_location",String)

)

class EmployeeIn(BaseModel) :
    emp_name: str
    emp_age : int
    emp_location:str

class EmployeeOut(EmployeeIn):
    emp_id : int

    

