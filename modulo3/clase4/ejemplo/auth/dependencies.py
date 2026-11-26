from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from auth.jwt import TokenInvalido, verificar_token
from core.database import get_db
from models.user import User
from repository.user_repository import UserRepository

security = HTTPBearer(auto_error=False) # Controlar errores

def _limpiar_token(token: str) -> str:
    token = toker.strip().strip('"').strip("'")
    if token.lower().startswith("bearer"): # lo pasa minuscula y revisa si empieza con bearer
        token = token[7:].strip()
    return token

async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    if credentials is None or credentials.scheme.lower() != "bearer": # si no esta el bearer
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Falta el token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    try:
        payload = verificar_token(_limpiar_token(credentials.credentials))
    except TokenInvalido as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=exc.detail,
            headers={"WWW-Authenticate": "Bearer"}
        )
    username = payload.get("sub")
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = UserRepository(db).get_by_username(username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,  # Cambié a 404 para "Usuario no encontrado"
            detail="Usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
    