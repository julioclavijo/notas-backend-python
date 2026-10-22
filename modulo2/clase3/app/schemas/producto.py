from decimal import Decimal
from pydantic import BaseModel, Field, field_validator

class _ProductoCampo(BaseModel):

    nombre: str = Field(
        min_length=1,
        max_length=120
    )
    precio: Decimal = Field(
        ge=0,
        max_digits=12,
        decimal_places=2
    )

    @field_validator("nombre")
    @classmethod
    def limpiar_nombre(cls, valor: str) -> str:
        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError("El nombre no puede estar en blanco")
        return valor_limpio


class ProductoEntrada(_ProductoCampo):
    stock: int = Field(default=0, ge=0) 

class ProductoActualizar(_ProductoCampo):
    stock: int = Field(ge=0)  # Solo validación mínima (>= 0)

class ProductoSalida(_ProductoCampo):
    model_config = ConfigDict(from_attributes=True)  # Configuración para datos de atributos
    id: int
    stock: int  # Sin validación adicional (solo tipo)