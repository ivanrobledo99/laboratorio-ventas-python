from database import base
from sqlalchemy import Column, Integer, String, Float,ForeignKey,Date,Time
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import date,time

class Producto(base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String,nullable=False)
    precio = Column(Float,nullable=False)


class ProductoCreate(BaseModel):
    nombre: str
    precio:float


class Venta(base):
    __tablename__="ventas"
    id=Column(Integer,primary_key=True,index=True)
    fecha=Column(Date,nullable=False)
    hora=Column(Time,nullable=False)
    id_carrito=Column(Integer,ForeignKey("Carritos.id"),unique=True, nullable=False)


class VentaCreate(BaseModel):
    fecha:date
    hora:time
    id_producto:int
    cantidad:int

class ProductoResponse(BaseModel):
    id:int
    nombre:str
    precio:float

    class Config:
        from_attributes=True

class VentaResponse(BaseModel):
    id:int
    fecha:date
    hora:time
    producto:ProductoResponse
    cantidad:int
    precio_total:float

    class Config:
        from_attributes=True

class Carrito(base):
    __tablename__="Carritos"
    id=Column(Integer, primary_key=True, index=True)
    fecha_creacion=Column(Date,nullable=False)
    estado=Column(String,nullable=False)

class Carrito_producto(base):
    __tablename__="Carrito_Producto"
    id=Column(Integer, primary_key=True, index=True)
    id_carrito=Column(Integer, ForeignKey("Carritos.id"), nullable=False)
    id_producto=Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad=Column(Integer,nullable=False)