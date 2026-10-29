from jose import jwt, ExpiredSignatureError, JWTError # Expiracion de jwt 
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("Falta el SECRET_KEY en el archivo .env")

ALGORITHM = "HS256"

# Crear un token de acceso con expiración de 30 minutos
def crear_token(datos: dict, expiration: int = 30) -> str:  
    to_encode = datos.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expiration)
    to_encode.update({"exp": expire}) # Añadir la expiración al token
    # retorna el token 
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Verifica el token deon jwt.decode
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
    datos_usuario = { 
        "sub": "usuario123",
        "rol": "admin"
    }

    token_generado = crear_token(datos_usuario)
    print("Token JWT generado:", token_generado)  
    print("\n*** Verificación de token ***")  
    datos_decodificados = verificar_token(token_generado)
    if datos_decodificados: 
        print("Token válido. Datos:", datos_decodificados)  

if __name__ == "__main__":
    main()
