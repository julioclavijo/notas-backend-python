from jose import jwt # Libreria de jtw
from datetime import datetime, timedelta, timezone # Libreria para manejar tiempo
import os
from dotenv import load_dotenv # dotenv para cargar variables de entorno

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY") # Variable de entorno para la clave secreta

if not SECRET_KEY:
    raise RuntimeError("Falta definir el secret key en .env")

ALGORITHM = "HS256" # Algoritmo de encriptación, hay varios 

# Metodo principal

def main():
    # payload
    data = {
        "sub": "usuario123", # sujeto
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30), # Expiración
    }

    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM) # Encriptación del payload
    print("Token generado:", token)

if __name__ == "__main__":
    main()

    