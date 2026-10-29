from passlib.context import CryptContext # Contexto de como se aplica passlib en codigo

from jose import jwt, ExpiredSignatureError, JWTError # Expiracion de jwt 
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()


HASH_SCHEME = "argon2" 
pwd_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto") 

def hash_password(password: str) -> str:
    return pwd_context.hash(password) 

def verify_password(plain_password: str, hashed_password: str):
    if not pwd_context.verify(plain_password, hashed_password):
        raise ValueError("Contraseña incorrecta")
    return True # revisar


SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("Falta el SECRET_KEY en el archivo .env")

ALGORITHM = "HS256"


def crear_token(datos: dict, expiration: int = 30) -> str:  
    to_encode = datos.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiration)
    to_encode.update({"exp": expire}) 
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        print("Error: El token ha expirado")
        return None
    except jwt.InvalidTokenError:
        print("Error: El token es inválido")
        return None

def main():
    
    # Registro
    password = "password123" # No recomendado
    print("Password: ", password)
    # Hash de la contraseña
    hashed = hash_password(password)
    print("Hash generado: ", hashed)
    
    # Login
    try: 
        verified = verify_password(password,hashed)
        print("Verificado: ", verified)
    except ValueError as e:
        print("Error: ", e)
        return
    USUARIO_REGISTRADO = "admin@email.com"
    
    # Entrega token
    datos = {"user": USUARIO_REGISTRADO,"rol": "administrador"} # Datos que
    token = crear_token(datos, 30)
    print("Token generado: ", token)

    # Acceso
    if verificar_token(token):
        print("Acceso permitido")
    else:
        print("Acceso denegado")


if __name__ == "__main__":
    main()