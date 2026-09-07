from database import base
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel

class Producto(base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    precio = Column(Float)


class ProductoCreate(BaseModel):
    nombre: str
    precio:float