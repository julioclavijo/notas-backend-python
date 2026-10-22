from fastapi import APIRouter, Depends, HTTPException, Query

from application.exceptions import NombreYaRegistrado, ProductoNoEncontrado, DatosInvalidosProducto
from application.services import ProductoService
from presentation.dependencies import get_producto_service
from app.schemas.producto import ProductoActualizar, ProductoEntrada, ProductoSalida

router = APIRouter(prefix="/productos", tags=["Productos"])

# Crea un nuevo producto con validación de datos y manejo de errores (conflicto 409 o datos inválidos 400)
@router.post("", response_model=ProductoSalida, status_code=201)
def crear_producto(
    entrada: ProductoEntrada,
    service: ProductoService = Depends(get_producto_service)
) -> ProductoSalida:
    try:
        producto = service.crear(**entrada.model_dump())
    except NombreYaRegistrado as error:
        raise HTTPException(status_code=409, detail="Nombre ya está registrado")
    except DatosInvalidosProducto as error:
        raise HTTPException(status_code=400, detail="Datos inválidos para el producto")
    return ProductoSalida.model_validate(producto)


@router.get("", response_model=list[ProductoSalida])
def listar_productos(
    desde: int = Query(default=0, ge=0),
    limite: int = Query(default=100, ge=1, le=100),
    service: ProductoService = Depends(get_producto_service)
) -> list[ProductoSalida]:
    productos = service.listar(desde=desde, limite=limite)
    return [ProductoSalida.model_validate(producto) for producto in productos] # Buscar, la funcion del for


# Endpoint para obtener un producto específico por ID, manejando error 404 si no existe
@router.get("/{producto_id}", response_model=ProductoSalida)
def obtener_producto(producto_id: int, service: ProductoService = Depends(get_producto_service)) -> ProductoSalida:
    try:
        producto = service.obtener(producto_id)
    except ProductoNoEncontrado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return ProductoSalida.model_validate(producto)