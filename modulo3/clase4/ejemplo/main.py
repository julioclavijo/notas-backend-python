import logging
import sys
from contextlib import asynccontextmanager # asincronas 
from pathlib import Path

from fastapi import FastAPI

APP_DIR = Path(__file__).resolve().parent
PROJECT_DIR = APP_DIR.parent
if str(PROJECT_DIR) not in sys.path: 
    sys.path.insert(0, str(PROJECT_DIR))

from core.database import init_db
from core.exceptions import register_exception_handlers
from core.logging import setup_logging
from core.middleware import add_middlewares
from routes.auth_routes import router as auth_router
from routes.user_routes import router as user_router

setup_logging()
logger = logging.getLogger(__name__)

# Configuracion de tablas
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    logger.info("Base de datos inicializada correctamente")
    yield
    logger.info("Aplicación finalizando...")

app = FastAPI(
    title="API de usuario",
    description="API para la gestión de usuarios con autenticación",
    version="1.0.0",
    lifespan=lifespan,
)

add_middlewares(app)
register_exception_handlers(app)
app.include_router(auth_router, prefix="/api/v1")
app.include_router(user_router, prefix="api/v1")


def main():

    import threading # manejo de hilos
    import time
    import webbrowser

    import uvicorn
    host = "127.0.0.1"
    port = 8000

    def open_browser():
        time.sleep(1.5)
        webbrowser.open(f"http://{host}:{port}/docs")

    threading.Thread(target=open_browser, daemon=True).start()

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload_dirs=[str(PROJECT_DIR)],
        log_level="info"  
        )

if __name__ == "__main__":
    main()