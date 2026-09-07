from fastapi import FastAPI
from database import engine, base, SessionLocal
from models import Producto, ProductoCreate
app=FastAPI()

base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje":"Hola Mundo"}


@app.post("/productos")
def crear_producto(producto: ProductoCreate):
    db = SessionLocal()

    nuevo_producto = Producto(
        nombre=producto.nombre,
        precio=producto.precio
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    db.close()

    return nuevo_producto
