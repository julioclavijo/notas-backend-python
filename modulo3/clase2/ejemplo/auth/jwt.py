from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError, ExpiredSignatureError

from core.config import settings

class TokenInvalido(Exception):
    def __init__(self, detail:str):
        self.detail = detail
        super().__init__(detail)

def crear_token(data: dict, expiration: int = settings.access_token_expire_minutes) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiration)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def verificar_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=settings.algorithm)
    except ExpiredSignatureError as exc:
        raise TokenInvalido("Token expirado") from exc
    except JWTError as exc:
        raise TokenInvalido("Token inválido") from exc