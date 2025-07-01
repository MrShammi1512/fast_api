from fastapi import FastAPI, HTTPException
from crud import ProductResource
from models import ProductIn, ProductOut
from database import database as db
from contextlib import asynccontextmanager
from sqlalchemy import MetaData, Table, Column, Integer, String, Float

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




@app.post("/product/add_product/", response_model=ProductOut)
async def addProduct(product_in : ProductIn):
   return await ProductResource.add_product(product_in)


@app.get("/product/", response_model=list[ProductOut])
async def getProduct():
    print("Calling get all product")
    return await ProductResource.get_all_product()

@app.get("/product/{product_id}", response_model=ProductOut)
async def getProductById(product_id :int):
    result= await ProductResource.get_product_by_id(product_id)
    if(result):
        return result
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/product/update-product/{product_id}", response_model=ProductOut)
async def updateProductDetail(product_id : int, product_in : ProductIn):
    return await ProductResource.update_product(product_id, product_in)


@app.delete("/product/delete/{product_id}")
async def deleteProduct(product_id:int):
    deleted= await ProductResource.delete_product(product_id)
    if deleted : 
        return {"Message :", f"Product with {product_id} deleted"}
    raise HTTPException(status_code=404,  detail ="Product not found")




  


