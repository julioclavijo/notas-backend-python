import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    # Manejador global de excepciones
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        if isinstance(exc, HTTPException):
            raise exc
        
        logger.exception("Error no manejado en %s", request.url.path)
        return JSONResponse(
            status_code=500, 
            content={"detail": "Error interno del servidor"}
        )
