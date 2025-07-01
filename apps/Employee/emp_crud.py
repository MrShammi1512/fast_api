from apps.database import database as db
from apps.Employee.emp_model import EmployeeIn, employee

class EmployeeResource:
    def __init__(self):
        pass

    @staticmethod
    async def get_employee_list() :
        try: 
            query = employee.select()
            employees= await db.fetch_all(query)
        
        except Exception as E:
            raise E
        
        return [dict(emp) for emp in employees]
    

    @staticmethod
    async def get_employee_by_id(emp_id : int):
        try : 
            query= employee.select().filter(employee.c.emp_id == emp_id)
            result= await db.fetch_one(query)

        except Exception as e :
            raise e
        
        return result
    
    @staticmethod
    async def add_employee(employeeIn : EmployeeIn):
        try :
            query= employee.insert().values(** employeeIn.dict())
            emp_id= await db.execute(query)
        except Exception as E :
            raise E
        
        return {**employeeIn.dict(), "emp_id" : emp_id}
    

    @staticmethod 
    async def updateEmployeeDetials(emp_id : int, employeeIn : EmployeeIn):
        try :
            query = employee.update().where(employee.c.emp_id==emp_id).values(**employeeIn.dict())
            result= await db.execute(query)
            updated =  await db.fetch_one(employee.select().where(employee.c.emp_id==emp_id))

        except Exception as E :
            raise E
        return dict(updated) if updated else None
    
    @staticmethod
    async def delete_employee(emp_id  : int):
        try : 
            query = employee.delete().where(employee.c.emp_id==emp_id)
            result =await db.execute(query)

        except Exception as E :
            raise E
        return {"message" : f"Employee with emp _id {emp_id} deleted"}



