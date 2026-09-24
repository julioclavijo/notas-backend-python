from fastapi import APIRouter, HTTPException, status
from models import TareaEntrada, TareaSalida, TareaUpdate
from typing import List

router = APIRouter()

tarea_db = []
id_actual = 1

@router.post("/tareas", response_model=TareaSalida)
def crea_tarea(tarea: TareaEntrada):
    global id_actual
    nueva_tarea = TareaSalida(
        id=id_actual,
        titulo=tarea.titulo,
        descripcion=tarea.descripcion,
        completada=False
    )
    tarea_db.append(nueva_tarea)
    id_actual += 1
    return nueva_tarea

@router.get("/tareas", response_model=List[TareaSalida])
def listar_tareas():    
    return tarea_db

@router.put("/tareas/{id}", response_model=TareaSalida, response_description="Tarea actualizada", summary="Actualizar una nota")
def actualiza_tarea(id: int, tarea: TareaUpdate):
    if id <= 0:
        raise HTTPException(status_code=422, detail="Id de Nota no valido")
    for indice, nota in enumerate(tarea_db):
        if nota.id == id:
            cambios = tarea.model_dump(exclude_unset=True, exclude={"id"})
            tarea_actualizada = nota.model_copy(update=cambios)
            tarea_db[indice] = tarea_actualizada
            return tarea_actualizada
    raise HTTPException(status_code=404, detail="Recurso no encontrado")

@router.delete("/tareas/{id}", status_code=status.HTTP_200_OK, summary="Eliminar una nota")
async def elimina_tarea(id: int):
    global tarea_db
    for nota in tarea_db:
        if nota.id == id:
            tarea_db.remove(nota)
            return {"message": "Nota eliminada"}
    raise HTTPException(status_code=404, detail="Nota no encontrada")