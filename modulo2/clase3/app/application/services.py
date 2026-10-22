# Services.py Recoge la solicitud
from decimal import Decimal
from sqlalchemy.orm import Session

# Importe local
from application.exceptions import (
    DatosInvalidosProducto,
    NombreYaRegistrado,
    ProductoNoEncontrado,
)
from infrastructure.database import ping
from infrastructure.exceptions import ( 
    ErrorNombreDuplicado,
    ErrorRestriccion,
)
from infrastructure.models import Producto
from infrastructure.repositories import ProductoRepository

class ProductoService:
    def __init__(self, repository: ProductoRepository) -> None:
        self.repository = repository
    
    # Opcion de crear los prouctos
    def crear(self, nombre: str, precio: Decimal, stock: int) -> Producto:
        producto = Producto(nombre=nombre, precio=precio, stock=stock)
        try:
            return self.repository.agregar(producto)
        except ErrorNombreDuplicado:
            raise NombreYaRegistrado() from None
        except ErrorRestriccion:
            raise DatosInvalidosProducto() from None
    
    # Opcion de listar los productos
    def listar(self, desde: int = 0, Limite: int = 100) -> list[Producto]:
        return self. repository.listar(desde=desde, Limite=Limite)

    # Opcion de obtener un producto por su ID
    def obtener(self, producto_id: int) -> Producto:
        producto = self.repository.obtener_por_id(producto_id)
        if producto is None:
            raise ProductoNoEncontrado()
        return producto

    # Opcion de actualizar un producto
    def actualizar(self, producto_id: int, nombre: str, precio: Decimal, stock: int) -> Producto:
        try:
            producto = self.repository.actualizar(producto_id, nombre, precio, stock)
        except ErrorNombreDuplicado:
            raise NombreYaRegistrado() from None
        except ErrorRestriccion:
            raise DatosInvalidosProducto() from None
        if producto is None:
            raise ProductoNoEncontrado()
        return producto

    # Opcion de eliminar un producto
    def eliminar(self, producto_id: int) -> None:
        if not self.repository.eliminar(producto_id):
            raise ProductoNoEncontrado( )

class SaludService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def verificar_base_de_datos(self) -> dict[str, str]:
        ping(self.session)
        return {"base_de_datos": "conectada"}