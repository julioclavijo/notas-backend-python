from passlib.context import CryptContext # Contexto de como se aplica passlib en codigo

HASH_SCHEME = "argon2" # Algoritmo de hash que se va a usar

# Creación del contexto de hashing
pwd_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto") 

def hash_password(password: str) -> str:
    return pwd_context.hash(password) # Devuelve el hash de la contraseña

def verify_password(plain_password: str, hashed_password: str):
    if not pwd_context.verify(plain_password, hashed_password): # Devuelve True si la contraseña es correcta
        raise ValueError("Contraseña incorrecta")

def main():
    print("*** Registro de usuarios ***")  
    password_registro = input("Introduzca una contraseña para registrar: ")
    hashed = hash_password(password_registro)
    print(f"Hash generado: {hashed}")  # No recomendado
    print("\n*** Prueba de contrasena ***")
    try:
        verify_password(password_registro, hashed)
        print("Contraseña correcta. Login exitoso.")
    except ValueError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()

