from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()
reservas: Dict[int, dict] = {} # diccionario vacio


class ReservaBase(BaseModel):
    huesped: str
    habitacion: int
    precio_noche: float
    notas: str | None = None

class ReservaCrear(ReservaBase):
    pass

class ReservaActualizar(BaseModel):
    huesped: str | None = None
    habitacion: int | None = None
    precio_noche: float | None = None
    notas: str | None = None

class ReservaRespuesta(ReservaBase):
    id: int

@app.get("/")
def raiz():
    return JSONResponse(
        status_code=200,
        content={"exitos": True, "mensaje": "Bienvenidos"}
    )

@app.get("/reservas/", response_model=List[ReservaRespuesta])
def obtener_todos_reservas():
    if not reservas:
        return JSONResponse(
            status_code=404,
            content={"exitos": False, "mensaje": "No se encontraron reservas"}
        )
    lista_reservas = [ReservaRespuesta(id=reserva_id, **datos).model_dump() for reserva_id, datos in reservas.items()]
    return JSONResponse(
        status_code=200,
        content={"exitos": True, "reservas": lista_reservas}
    )

@app.get("/reservas/{id}", response_model=ReservaRespuesta)
def obtener_reserva(reserva_id: int):
    if reserva_id not in reservas:
        return JSONResponse(
            status_code=404,
            content={"exitos": False, "mensaje": "articuos no encotrado"}
        )
    return JSONResponse(
        status_code=200,
        content={"exitos": True, "reserva": ReservaRespuesta(id=reserva_id, **reservas[reserva_id]).model_dump()}
    )

@app.post("/reservas/", response_model=ReservaRespuesta)
def crear_reserva(reserva: reservaCrear):
    global contador_reservas
    reserva_id = contador_reservas
    contador_reservas += 1
    reservas[reserva_id] = reserva.model_dump()
    return JSONResponse(
        status_code=200,
        content={
            "exitos": True, 
            "mensaje": "reserva creado", 
            "reserva": ReservaRespuesta(id=reserva_id, **reservas[reserva_id]).model_dump()}
    )

@app.put("/reservas/{reserva_id}", response_model=ReservaRespuesta)
def actualizar_reserva(reserva_id: int, reserva: reservaActualizar):
    if reserva_id not in reservas:
        return JSONResponse(
            status_code=404,
            content={"exito": False, "mensaje": "Artículo no encontrado"}
                )
    reserva_guardado = reservas[reserva_id]
    datos_actualizados = reserva.model_dump(exclude_unset=True)
    reserva_guardado.update(datos_actualizados)
    reservas[reserva_id] = reserva_guardado

    return JSONResponse(
        status_code=200,
        content={
            "exitos": True,
            "mensaje": "reserva creado", 
            "reserva": ReservaRespuesta(id=reserva_id, **reserva_guardado).model_dump()
        }
    )

@app.delete("/reservas/{reserva_id}")
def eliminar_reserva(reserva_id: int):
    if reserva_id not in reservas:
        return JSONResponse(
            status_code=404,
            content={"exito": False, "mensaje": "Artículo no encontrado"}
            )
    reserva_eliminado = reservas.pop(reserva_id)
    return JSONResponse(
        status_code=200,
        content={
            "exitos": True,
            "mensaje": "reserva {reserva_id} eliminado",
            "reserva": ReservaRespuesta(id=reserva_id, **reserva_eliminado).model_dump()
        }
    )
