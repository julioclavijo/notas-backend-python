# Lo primero aparece cuando abre Uvicorn

from fastapi import APIRouter
router = APIRouter(tags=["raiz"])

@router.get("/")
def raiz() -> dict[str, str]:
    return {
        "mensaje": "Catálogo de productos",
        "documentacion": "/docs",
        "productos": "/productos",
        "salud": "/salud/db"
    }