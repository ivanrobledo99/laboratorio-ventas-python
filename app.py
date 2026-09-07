from fastapi import FastAPI
from database import engine, base
from models import Producto, ProductoCreate
app=FastAPI()

base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje":"Hola Mundo"}


@app.post("/productos")
def crear_producto(producto: ProductoCreate):
    return producto 
