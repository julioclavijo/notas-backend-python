from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator

def normalizar_username(value: str) -> str:
    return value.strip().lower()

class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Recomendado para Pydantic v2

    username: str = Field(
        ...,
        min_length=3,  
        max_length=50,  
        description="Nombre de usuario único",  
        example="juan_perez" 
    )
    password: str = Field(
        ...,
        min_length=6,  
        description="Contraseña del usuario",  
        example="miPassword123" 
    )

    @field_validator("username")
    @classmethod
    def username_normalizado(cls, value: str) -> str:
        return normalizar_username(value)

class UserLogin(BaseModel) :
    username: str = Field(..., description="Nombre de usuario", examples=["juan_perez"])
    password: str = Field(..., description="Contrasefna del usuario", examples=["miPassword123"])
    @field_validator
    @classmethod
    def username_normalizado(cls, value: str) -> str:
        return normalizar_username(value)

class UserResponse(BaseModel) :
    id: int = Field(examples=[1])
    username: str = Field(examples=["juan_perez"])
    created_at: Optional[datetime] = Field(default=None, examples=["2026-11-11T19:49:00"])
    updated_at: Optional[datetime] = Field(default=None, examples=[None])

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel) :
    access_token: str = Field(..., description="Token JWT de acceso", examples=["eyJhbGci0iJIUZIINiIsInRScCI61kpxVCI9..."])
    token_type: str = Field(default="bearer", description="Tipo de token", examples=["bearer"])

class LoginResponse(BaseModel):
    access_token: str = Field(..., description="Token JWT de acceso", examples=["eyJhbGci0iJIUZIINiIsInRScCI61kpxVCI9..."])
    token_type: str = Field(default="bearer", description="Tipo de token", examples=["bearer"])
    user: UserResponse = Field(..., description="Datos del usuario autenticado")
class Message(BaseModel1): 
    mensaje: str = Field(exampLes=["Operacion realizada con éxitos"])