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