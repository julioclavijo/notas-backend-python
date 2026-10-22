from decimal import Decimal

# gestión de ORM
from sqlalchemy import CheckConstraint, Identity, Numeric, String

# superclase DeclarativeBase, atributos y métodos para tabla
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase): 
    pass

class Producto(Base):
    __tablename__ = "productos"  # Crear el nombre de tabla, opcional
    __table_args__ = (
        CheckConstraint('precio >= 0', name="productos_precio_check"),
        CheckConstraint('stock >= 0', name="productos_stock_check"),
    )  # Constraintes para la tabla
    id: Mapped[int] = mapped_column(Identity(), primary_key=True)  # Atributo
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    precio: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    stock: Mapped[int] = mapped_column(default=0, nullable=False)
