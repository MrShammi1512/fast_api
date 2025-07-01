from database import database as db
from models import ProductIn, ProductOut, product




class ProductResource : 
    def __init__(self):
        pass

    @staticmethod
    async def add_product(product_in : ProductIn):
        try:
           query= product.insert().values(**product_in.dict())
           product_id= await db.execute(query)

        
        except Exception as e :
          
            raise e
        
        return {**product_in.dict(),"id":product_id}
    
    @staticmethod
    async def get_all_product():
        try :
            query= product.select()
            rows= await db.fetch_all(query)
        
        except Exception as e : 
            raise e
       

        return [dict(row) for row in rows]
    
    @staticmethod
    async def get_product_by_id (product_id):
        try : 
           query= product.select().where(product.c.id==product_id)
           row= await db.fetch_one(query)

          

        except Exception as e : 
            raise e 
        
        return dict(row) if row else  None
    
    @staticmethod
    async def update_product(product_id, product_in):
        try : 
            query= product.update().where(product.c.id == product_id).values(**product_in.dict())
            result= await db.execute(query)

            updated= await  db.fetch_one(product.select().where(product.c.id ==product_id))


        except Exception as e :
            raise e
        return  dict(updated) if updated else None
    
    @staticmethod
    async def delete_product(product_id :int):
        try:
            query = product.delete().where(product.c.id == product_id)
            result= await db.execute(query)



        except Exception as e :
            raise e
        
        return {"message": f"Product with id {productId} deleted."}
        


   



