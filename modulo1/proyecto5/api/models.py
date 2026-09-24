from pydantic import BaseModel, Field
from typing import Optional 

class TareaBase(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100, description="Nombre de la nota", examples=["Cena el viernes"])
    descripcion: Optional[str] = Field(None, max_length=200, description="Descripción opcional del recurso", examples=["Cena el cliente el miercoles al 8pm"])

class TareaEntrada(TareaBase):
    pass

class TareaSalida(BaseModel):
    id: int = Field(..., gt=0, description="Id de la nota")
    titulo: str
    descripcion: Optional[str] = None
    completada: bool

class TareaUpdate(BaseModel):
    id: Optional[int] = Field(None, gt=0, description="Id de la nota")
    titulo: Optional[str] = Field(None, min_length=3, max_length=100, description="Nombre de la nota", examples=["Cena el viernes"])
    descripcion: Optional[str] = None
    completada: Optional[bool] = None

