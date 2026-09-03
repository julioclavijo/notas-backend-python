# Introduccion

Proyecto1
##  Configuracion de entorno
Se usa el requierements.txt `pip install -r requirements.txt`
Librerias uvicorn
`pip install fastapi uvicorn`

### Ejemplo inicial
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def inicio():
    return {"mensaje": "¡Hola,"}
```

### Ejecucion
`uvicorn main:app --reload`


Proyecto2
## Ejemplo 2

Que es un dataclases
```python
from dataclasses import dataclass
@dataclass
class Producto: nombre: str precio: float cantidad: int = 8
```

Importacion de los modelos
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
```

Luego http://127.0.0.1:8000/docs
prueba de la api

## Ejercicio 1
API de Gestion de Productos
Objetivo: Crear una API REST para gestionar un inventario de productos escolares o tecnoldgicos. 

Instrucciones:
Modifica el codigo base reemplazando la entidad Cliente por una entidad Producto. El sistema debe cumplir con los siguientes requerimientos: 
1. Modelo de Datos (Producto): 
    o id: Entero (autoincremental). 
    o nombre: Cadena de texto (string). 
    o precio: Numero decimal (float). 
    o stock: Entero (int). 
2. Endpoints a implementar: 
    o GET/: Mensaje de bienvenida. 
    o POST /productos: Crear un producto (generando el ID automaticamente). 
    o GET /productos: Listar todos los productos. 
    o GET/productos/{producto_id}: Buscar un producto por ID (lanzar error 404 si no existe). 
    o PUT/productos/{producto_id}: Actualizar el nombre, precio y stock de un producto existente (lanzar error 404 si no existe).
    o DELETE /productos/{producto_ id}: Eliminar el producto (lanzar error 404 si no existe).