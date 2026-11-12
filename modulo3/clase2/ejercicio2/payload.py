from jose import jwt, ExpiredSignatureError, JWTError
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()

# Configuracion  de variables globales
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("Falta el SECRET_KEY en el archivo .env")

ALGORITHM = "HS256"
EXPIRE = 15

# Contruccion del payload y tiempo de expiracion


# Expiracion de 15 minutos
def crear_token(payload: dict, expiration: int = EXPIRE) -> str:  
    to_encode = payload.copy()
    # colocar el timestamp
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
    # Revisar estructura
    payload = { 
        "idUser": "4371",
        "fullname": "User Home",
        "rol": "admin"
    }

    token_generado = crear_token(datos_usuario)
    


    print("\n*** Verificación de token ***")  
    datos_decodificados = verificar_token(token_generado)
    if datos_decodificados: 
        print("Token válido. Datos:", datos_decodificados)  

if __name__ == "__main__":
    main()
