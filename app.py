from fastapi import FastAPI, HTTPException
from database import engine, base, SessionLocal
from models import Producto, ProductoCreate, Venta, VentaCreate, VentaResponse, ProductoResponse
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
        db.close()
        raise HTTPException(status_code=404, detail="PRODUCTO NO ENCONTRADO")

    db.close()
    return producto
    
@app.put("/productos/{id}")
def Agregar_Producto_ID(id:int, producto:ProductoCreate):
    db=SessionLocal()

    producto_db=db.query(Producto).filter(Producto.id==id).first()

    if producto_db is None:
        db.close()
        raise HTTPException(status_code=404, detail="PRODUCTO NO ENCONTRAOD")

    producto_db.nombre=producto.nombre
    producto_db.precio=producto.precio

    db.commit()

    db.close()
    return producto_db


@app.delete("/productos/{id}",response_model=ProductoResponse)
def Eliminar_Producto(id:int):
    db=SessionLocal()

    producto_db=db.query(Producto).filter(Producto.id==id).first()

    if producto_db is None:
        db.close()
        raise HTTPException(status_code=404, detail="PRODUCTO NO ENCONTRADO")

    db.delete(producto_db)
    db.commit()

    db.close()
    return producto_db


@app.post("/ventas",response_model=VentaResponse)
def Crear_Venta(ventas:VentaCreate):
    db=SessionLocal()

    producto_db=db.query(Producto).filter(Producto.id == ventas.id_producto).first()

    if producto_db is None:
            db.close()
            raise HTTPException(status_code=404, detail="PRODUCTO NO ENCONTRADO")
    

    Nueva_venta=Venta(
        fecha=ventas.fecha,
        hora=ventas.hora,
        id_producto=ventas.id_producto,
        cantidad=ventas.cantidad,
        precio_total=producto_db.precio*ventas.cantidad
    )

    
    db.add(Nueva_venta)
    db.commit()
    db.refresh(Nueva_venta)

    Nueva_venta.producto

    db.close()

    return Nueva_venta


@app.get("/ventas")
def Obtener_ventas():
    db=SessionLocal()

    Ventas_db=db.query(Venta).all()
    db.close()

    return Ventas_db


@app.get("/ventas/{id}",response_model=VentaResponse)
def Obtener_venta_id(id:int):
    db=SessionLocal()

    Venta_db_id=db.query(Venta).filter(Venta.id == id).first()

    if Venta_db_id is None:
        db.close()
        raise HTTPException(status_code=404, detail="VENTA NO ENCONTRADA")

    Venta_db_id.producto

    db.close()

    return Venta_db_id

@app.delete("/ventas/{id}")
def Eliminar_venta(id:int):
    db=SessionLocal()

    Venta_eliminar=db.query(Venta).filter(Venta.id == id).first()

    if Venta_eliminar is None:
        db.close()
        raise HTTPException(status_code=404, detail="Venta no encontrada")


    db.delete(Venta_eliminar)
    db.commit()
    db.close()

    return

@app.put("/ventas/{id}",response_model=VentaResponse)
def Agregar_Venta(id:int,venta:VentaCreate):
    db=SessionLocal()

    Nueva_venta=db.query(Venta).filter(Venta.id == id).first()

    if Nueva_venta is None:
        db.close()
        raise HTTPException(status_code=404, detail="VENTA NO ENCONTRADA")

    producto_db=db.query(Producto).filter(Producto.id == venta.id_producto).first()

    if producto_db is None:
        db.close()
        raise HTTPException(status_code=404, detail="PRODUCTO NO ENCONTRADO")
    
    Nueva_venta.fecha=venta.fecha
    Nueva_venta.hora=venta.hora
    Nueva_venta.id_producto=venta.id_producto
    Nueva_venta.cantidad=venta.cantidad
    Nueva_venta.precio_total=venta.cantidad*producto_db.precio

    db.commit()
    db.refresh(Nueva_venta)

    Nueva_venta.producto
    db.close()
    
    return Nueva_venta