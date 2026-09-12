from database import base
from sqlalchemy import Column, Integer, String, Float,ForeignKey,Date,Time
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import date,time

class Producto(base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    precio = Column(Float)
    ventas=relationship("Venta", back_populates="producto")


class ProductoCreate(BaseModel):
    nombre: str
    precio:float


class Venta(base):
    __tablename__="ventas"
    id=Column(Integer,primary_key=True,index=True)
    fecha=Column(Date)
    hora=Column(Time)
    id_producto=Column(Integer,ForeignKey("productos.id"))
    cantidad=Column(Integer)
    precio_total=Column(Float)
    producto=relationship("Producto", back_populates="ventas")


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
