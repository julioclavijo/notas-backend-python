from fastapi import Depends
from sqlalchemy.orm import Session
from application.services import ProductoService, SaludService
from infrastructure.database import get_session
from infrastructure.repositories import ProductoRepository

def get_producto_service(session: Session = Depends(get_session)) -> ProductoService:
    return ProductoService(ProductoRepository(session))

def get_salud_service(session: Session = Depends(get_session)) -> SaludService:
    return SaludService(session)