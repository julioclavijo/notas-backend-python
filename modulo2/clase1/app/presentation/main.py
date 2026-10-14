from fastapi import FastAPI
from app.api.productos import router as productos_router 
from app.api.raiz import router as raiz_router 
from app.infrastructure.database import crear_tablas

# crear tablas antes de:
crear_tablas() 

app = FastAPI(title="Catalogo de productos")
app.include_router(raiz_router) 
app.include_router(productos_router)