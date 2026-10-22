from fastapi import FastAPI
from api.productos import router as productos_router
from api.raiz import router as raiz_router
from infrastructure.database import crear_tablas

# crear tablas antes de:
crear_tablas()

app = FastAPI(title="Catalogo de productos")
app.include_router(raiz_router)
app.include_router(productos_router)
