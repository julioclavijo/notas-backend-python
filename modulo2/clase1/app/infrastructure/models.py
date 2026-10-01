from decimal import Decimal

from sqlalchemy import CheckConstraint, Identity, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# declaracion de la clase base
class Base(DeclarativeBase):
    pass

class Producto(Base):
    # crea el nombre de la tabla
    __tablename__ = 'productos'
    __table_args__= (
        CheckConstraint('precio >= 0', name='productos_precio_check'),
        CheckConstraint('stock >= 0', name='productos_stock_check'),
    )
    # El mapped por el tipado
    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(length=50), unique=True, nullable=False)
    precio: Mapped[Decimal] = mapped_column(Numeric(12,2), nullable=False)
    stock: Mapped[int] = mapped_column(default=0, nullable=False)