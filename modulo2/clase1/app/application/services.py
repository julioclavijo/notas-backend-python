from decimal import Decimal 
from sqlalchemy.orm import Session

from application.exceptions import NombreYaRegistrado, ProductoNoEncontrado, DatosInvalidosProducto 
from infrastructure.database import ping 
from infrastructure.exceptions import ErrorNombreDuplicado, ErrorRestriccion
from infrastructure.models import Producto 
from infrastructure.repositories import ProductoRepository 

class ProductoService:
    def __init__(self, repository: ProductoRepository) -> None:
        self.repository = repository

    def crear(self, nombre: str, precio: Decimal, stock: int) -> Producto:
        producto = Producto(nombre=nombre, precio=precio, stock=stock)
        try:
            return self.repository.agregar(producto)
        except ErrorNombreDuplicado:
            raise NombreYaRegistrado() from None
        except ErrorRestriccion:
            raise DatosInvalidosProducto() from None

    def listar(self) -> list[Producto]:
        return self.repository.listar()

    def obtener_por_id(self, producto_id: int) -> Producto:
        producto_id = self.repository.obtener_por_id(producto_id)
        if producto is None:
            raise ProductoNoEncontrado()
        return producto

class SaludService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def verificar_base_de_datos(self) -> dict[str, str]:
        ping(self.session)
        return {'base de datos': 'conectada'}