from apps.Employee.emp_model import EmployeeIn, EmployeeOut
from apps.Employee.emp_crud import EmployeeResource
from apps.database import database as db
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/employee", response_model=list[EmployeeOut])
async def getAllEmployees():
    return await EmployeeResource.get_employee_list()

@app.get("/employee/{emp_id}", response_model=EmployeeOut)
async def getEmployee(emp_id):
    return await EmployeeResource.get_employee_by_id(emp_id)

@app.post("/employee", response_model=EmployeeOut)
async def addEmployee(employeeIn :EmployeeIn ):
    return await EmployeeResource.add_employee(employeeIn)

@app.put("/employee/{emp_id}",response_model=EmployeeOut)
async def updateEmployee(emp_id : int, employeeIn : EmployeeIn):
    return await EmployeeResource.updateEmployeeDetials(emp_id, employeeIn)

@app.delete("/employee/{emp_id}")
async def deleteEmployee(emp_id  : int):
    return await EmployeeResource.delete_employee(emp_id)
