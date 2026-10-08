from fastapi import APIRouter, Depends, HTTPException
from application.exceptions import DatosInvalidosProducto, ProductoNoEncontrado, NombreYaRegistrado 
from application.services import ProductoService
from presentation.dependencies import get_producto_service
from schemas.producto import ProductoEntrada, ProductoSalida

router = APIRouter(prefijo="/productos", tags=["Productos"]) # prefijo: se añade a la raiz de la ruta
# para documentar se usa tags=["Productos"], pero se usa otras librerias

@router.post("", response_modeL=ProductoSalida, status_code=201) 
def crear_producto(
    entrada: ProductoEntrada,
    service: ProductoService = Depends(get_producto_service) ) -> ProductoSalida:
    try: producto = service.crear(**entrada.model_dump()) 
    except NombreYaRegistrado:
        raise HTTPException(status_code=409, detail="Nombre ya registrado") from None 
    except DatosInvalidosProducto:
        raise HTTPException(status_code=400, detail="Datos invalidos para el producto") from None 
    return ProductoSalida.model_validate(producto)


@router.get("", response_modeL=list[ProductoSalida] )
def listar_productos(service: ProductoService = Depends(get_producto_service)) -> list[ProductoSalida]:
    return[ProductoSalida.model_validate(producto) for producto in service.listar()]

@router.get("/{producto_id}", response_modeL=ProductoSalida)
def obtener_producto(producto_id: int, service: ProductoService = Depends(get_producto_service)) -> ProductoSalida:
    try:
        producto = service.obtener(producto_id)
    except ProductoNoEncontrado:
        raise HTTPException(status_code=404, detail="Producto no encontrado") from None 
    return ProductoSalida.model_validate(producto)