from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Creacion de modelo
class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int

producto_db: List(Producto) = []
contador_id = 1


@app.get("/")
async def inicio():
    return {"mensaje:", "Bienvenido"}

# Crear un producto
@app.post("/productos", response_model=Producto)
async def crear_producto(producto: Producto):
    global contador_id
    producto.id = contador_id
    producto_db.append(producto)
    contador_id += 1
    return producto

# Consultar todos los productos
@app.get("/productos", response_model=List[Producto])
async def listar_productos():
    return producto_db

# Buscar un producto por id
@app.get("/productos/{producto_id}", response_model=Producto)
async def obtener_producto(producto_id: int):
    for producto in producto_db:
        if producto.id == producto_id:
            return producto
    # la excepcion se envia al controlador de fastapi
    raise HTTPException(status_code=404, detail="Producto no encontrado") 

# actualizar un registro
@app.put("/productos/{producto_id}", response_model=Producto)
async def actualizar_producto(producto_id: int, producto_actualizado: Producto):
    for producto in producto_db:
        if producto.id == producto_id:
            producto.nombre = producto_actualizado.nombre
            producto.precio = producto_actualizado.precio
            producto.stock  = producto_actualizado.stock
            return producto
    # Si no lo consigue
    raise HTTPException(status_code=404, detail="Producto no encontrado")

# eliminar el registro productos
@app.delete("/Producto/{producto_id}")
async def eliminar_Producto(producto_id: int):
    for producto in producto_db:
        if producto.id == producto_id:
            producto_db.remove(producto)
            return {"mensaje": f"Producto {producto.id} eliminado"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")