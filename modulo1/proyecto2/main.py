from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Creacion de modelo
class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int

cliente_db: List(Cliente) = []
contador_id = 1

@app.get("/")
async def inicio():
    return {"mensaje:", "¡Hola,"}

# Crear un cliente
@app.post("/cliente", response_model=Cliente)
async def crear_cliente(cliente: Cliente):
    global contador_id
    cliente.id = contador_id
    cliente_db.append(cliente)
    contador_id += 1
    return cliente

# Consultar todos los clientes
@app.get("/clientes", response_model=List[Cliente])
async def listar_clientes():
    return cliente_db

@app.get("/cliente/{cliente_id}", response_model=Cliente)
async def obtener_cliente(cliente_id: int):
    for cliente in cliente_db:
        if cliente.id == cliente_id:
            return cliente
    # la excepcion se envia al controlador de fastapi
    raise HTTPException(status_code=404, detail="Cliente no encontrado") 

# actualizar un registro
@app.put("/cliente/{cliente_id}", response_model=Cliente)
async def actualizar_cliente(cliente_id: int, cliente_actualizado: Cliente):
    for cliente in cliente_db:
        if cliente.id == cliente_id:
            cliente.nombre = cliente_actualizado.nombre
            cliente.edad = cliente_actualizado.edad
            return cliente
    # Si no lo consigue
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# eliminar el registro
@app.delete("/cliente/{cliente_id}")
async def eliminar_cliente(cliente_id: int):
    for cliente in cliente_db:
        if cliente.id == cliente_id:
            cliente_db.remove(cliente)
            return {"mensaje": f"Cliente {cliente.id} eliminado"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")