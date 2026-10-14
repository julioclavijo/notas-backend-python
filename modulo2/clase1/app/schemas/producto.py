from decimal import Decimal 
from pydantic import BaseModel, ConfigDict, Field, field_validator # revirsar

class ProductoEntrada(BaseModel) : 
    nombre: str = Field(min_Length=1, max_Length=120)
    precio: Decimal = Field(ge=0, max_digits=12, decimal_places=2)
    stock: int = Field(default=0, ge=0)

    @field_validator('nombre') # validar el atributo definido en las comillas
    @classmethod
    def limpiar_nombre(cls, valor: str) -> str:
        valor_limpio = valor.strip() # strip para limpiar las cadenas de texto
        if not valor_limpio:
            raise ValueError("El nombre no puede estar vacío")
        return valor_limpio

class ProductoSalida(ProductoEntrada):
    model_config = ConfigDict(from_attributes=True) # convierte los atributos de la clase a los atributos de la base
    id: int