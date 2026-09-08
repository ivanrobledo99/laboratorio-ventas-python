from fastapi import FastAPI, HTTPException
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

@app.get("/productos")
def Obtener_Producto():
    db=SessionLocal()

    productos=db.query(Producto).all()

    db.close()
    return productos

@app.get("/productos/{id}")
def Obtener_Producto_id(id: int):
    db=SessionLocal()

    producto=db.query(Producto).filter(Producto.id==id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="PRODUCTO NO ENCONTRADO")

    db.close()
    return producto
    
@app.put("/productos/{id}")
def Agregar_Producto_ID(id:int, producto:ProductoCreate):
    db=SessionLocal()

    producto_db=db.query(Producto).filter(Producto.id==id).first()

    if producto_db is None:
        raise HTTPException(status_code=404, detail="PRODUCTO NO ENCONTRAOD")

    producto_db.nombre=producto.nombre
    producto_db.precio=producto.precio

    db.commit()

    db.close()
    return producto_db



