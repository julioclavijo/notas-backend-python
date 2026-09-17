from fastapi import FastAPI, APIRouter, HTTPException, status 
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional # por el tipado fuerte

class RecursoBase(BaseModel):
    nombre: str = Field(..., min_Length=3, max_Length=56, description="Nombre del recurso", exampLes=["Monitor Samsung"])
    descripcion: Optional[str] = Field(None, max_Length=200, description="Descripcon opcional del recurso", examples=["Monitor portatil para laptop"])

class RecursoCreate(RecursoBase):
    item_id: int = Field(..., gt=0, description="Identificador del recurso")

class RecursoUpdate(BaseModel): 
    nombre: Optional[str] = Field(None, min_Length=3, max_Length=50, exampLles=["Recurso actualizado"]) 
    descripcion: Optional[str] = Field(None, max_Length=200, description="Descripcon opcional del recurso", examples=["Nueva descripcion" ])

class RecursoResponse(RecursoBase ): 
    pass

class UsuarioBase(BaseModel): 
    username: str = Field(..., min_Length=4, max_Length=16, description="Nombre de usuario", exampLes=["juanchoElAvion" ]) 
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", description="Correo electronico valido", examples=["juanchoElAvion@ejemplo.com" ]) 
    edad: int = Field(..., gt=0, Lt=120, description="Edad entre 1 y 119 años", examples=[25])

class UsuarioCreate(UsuarioBase): 
    pass

class UsuarioUpdate(BaseModel): 
    username: Optional[str] = Field(None, min_Length=4, max_Length=16, exampLles=["Nuevo usuario" ])
    email: Optional[str] = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", description="Correo electronico valido", examples=["juanchoElAvion@ejemplo.com" ]) 
    edad: Optional[int] = Field(..., gt=0, Lt=120, description="Edad entre 1 y 119 años", examples=[25])

class UsuarioResponse(UsuarioBase): 
    user_id: int = Field(..., gt=0, description="ID Unico del usuario")

db_recursos: List[Dict] = [] 
next_recurso_id = 1

db_usuario: List[Dict] = [] 
next_usuario_id = 1

recursos_router = APIRouter(
    prefix="/recursos", 
    tags=["APIRecursos"], 
    responses={404: {"description": "Recurso no encontrado"}}
    )

usuarios_router = APIRouter(
    prefix="/usuarios", 
    tags=["APIusuarios"], 
    responses={404: {"description": "Usuario no encontrado"}}
    )


@recursos_router.post(
    "/",
    response_model=RecursoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un recurso nuevo"
)
# model_dump: convierte un objeto de modelo en un diccionario de Python (serialización)
async def create_recurso(recurso: RecursoCreate):
    global next_recurso_id
    new_item = recurso.model_dump()
    new_item["item_id"] = next_recurso_id
    db_recursos.append(new_item)
    next_recurso_id += 1
    return new_item

@recursos_router.get(
    "/",
    response_model=List[RecursoResponse],
    summary="Obtener todos los recursos"
)
async def get_all_recursos():
    return db_recursos

@recursos_router.get(
    "/{item_id}",
    response_model=RecursoResponse,
    summary="Obtener un recurso específico"
)
async def read_recurso(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=422, detail="ID de un recurso invalido")
    for item in db_recursos:
        if item["item_id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Recurso no encontrado" )

@recursos_router.put(
    "/{item_id}",
    response_model=RecursoResponse,
    summary="Actualizar un recurso"
)
async def update_recurso(item_id: int, recurso: RecursoUpdate):
    if item_id <= 0:
        raise HTTPException(status_code=422, detail="ID de un recurso invalido")
    for item in db_recursos:
        if item["item_id"] == item_id:
            update_data = recurso.model_dump(exclude_unset=True)
            item.update(update_data)
            return item
    raise HTTPException(status_code=404, detail="Recurso no encontrado")

@recursos_router.delete(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar un recurso"
)
async def delete_recurso(item_id: int):
    global db_recursos
    for item in db_recursos:
        if item["item_id"] == item_id:
            db_recursos.remove(item)
            return{"message": "Recurso eliminado"}
    raise HTTPException(status_code=404, detail="Recurso no encontrado")

# %Mejorar el modelo de recursos y completar las api de usuario

# ---
# Punto de entrada
# ---

app = FastAPI(
    title="Recursos API",
    description="Ejemplo de APIs con FastAPI para gestionar recursos, APIRouter personalizados, validacion con Pydantic y base en memoria",
    version="2.0.0",
)

@app.get("/", summary="Pagina de incio de la API")
async def read_root():
    return {
        "mensaje": "Bienvenido a la API de Recursos y Usuarios",
        "version": "2.0.0",
        "documentacion": "/docs",
        "endpoints":{
            "recursos": "/recursos",
            "usarios": "/usuarios"
        }
    }

app.include_router(recursos_router)
app.include_router(usuarios_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )