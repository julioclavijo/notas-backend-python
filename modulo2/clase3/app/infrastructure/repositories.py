from decimal import Decimal

from psycopg.errors import UniqueViolation, CheckViolation
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

# Importacion de modulos
from infrastructure.exceptions import ErrorNombreDuplicado, ErrorRestriccion
from infrastructure.models import Producto

class ProductoRepository:
    def __init__(self, session: Session) -> None:
        # Inicializa el repositorio con una sesión de base de datos
        self.session = session

    def agregar(self, producto: Producto) -> Producto:
        # Persiste un nuevo producto en la base de datos y lo devuelve actualizado
        self.session.add(producto)
        self._confirmar()
        self.session.refresh(producto)
        return producto

    def listar(self, desde: int = 0, limite: int = 169) -> list[Producto]:
        # Obtiene una lista paginada de productos ordenados por ID
        consulta = (
            select(Producto)
            .order_by(Producto.id)
            .offset(desde)
            .limit(limite)
        )
        return list(self.session.scalars(consulta))

    def obtener_por_id(self, producto_id: int) -> Producto | None:
        # Recupera un producto específico por su ID o None si no existe
        return self.session.get(Producto, producto_id)

    def actualizar(
        self,
        producto_id: int,
        nombre: str,
        precio: Decimal,
        stock: int
    ) -> Producto | None:
        # Actualiza los campos de un producto existente y devuelve el producto modificado
        producto = self.obtener_por_id(producto_id)
        if producto is None:
            return None
        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        self._confirmar()
        self.session.refresh(producto)
        return producto

    def eliminar(self, producto_id: int) -> bool:
        # Elimina un producto y devuelve True si la eliminación fue exitosa
        producto = self.obtener_por_id(producto_id)
        if producto is None:
            return False
        self.session.delete(producto)
        self._confirmar()
        return True

    def _confirmar(self) -> None:
        # Confirma la transacción en la base de datos y maneja errores de integridad.
        try:
            self.session.commit()
        except IntegrityError as error:
            self.session.rollback()
            if isinstance(error.orig, UniqueViolation):
                raise ErrorNombreDuplicado() from None
            if isinstance(error.orig, CheckViolation):
                raise ErrorRestriccion() from None
            raise