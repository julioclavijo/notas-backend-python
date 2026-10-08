# Importaciones de terceros
from psycopg.errors import UniqueViolation
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from infrastructure.exceptions import ErrorNombreDuplicado, ErrorRestriccion
from infrastructure.models import Producto

class ProductoRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def agregar(self, producto: Producto) -> Producto: 
        self.session.add(producto)
        try:
            self.session.commit()
        except IntegrityError as error:
            self.session.rollback()
            if isinstance(error.orig, UniqueViolation):
                raise ErrorNombreDuplicado() from None
            raise ErrorRestriccion() from None
        self.session.refresh(producto) # Actualiza el objeto con los cambios realizados
        return producto

    def listar(self) -> list[Producto]: 
        return list(self.session.scalars(select(Producto).order_by(Producto.id) ))

    def obtener_por_id(self, producto_id: int) -> Producto | None:
        return self.session.get(Producto, producto_id)