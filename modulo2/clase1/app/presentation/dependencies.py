from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services import ProductoService, SaludService
from app.infrastructure.database import get_session # validar la conexion a la db
from app.infrastructure.repositories import ProductoRepository

def get_producto_service(session: Session = Depends(get_session)) -> ProductoService:
    repository = ProductoRepository(session)
    return ProductoService(repository)

def get_salud_service(session: Session = Depends(get_session)) -> SaludService: # ve si hay una conexion con base de datos
    return SaludService(session)