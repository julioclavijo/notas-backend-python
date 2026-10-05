import os                  # Módulo para interactuar con el sistema operativo (variables de entorno, rutas, etc.).
from pathlib import Path   # Clase para manejar rutas de archivos de forma moderna y portable.
from collections.abc import Generator  # Tipo para indicar que una función puede devolver un generador (iterador).

from dotenv import load_dotenv  # Carga variables de entorno desde un archivo `.env`.
from sqlalchemy import create_engine, text  # `create_engine`: crea conexión a la BD; `text`: para consultas SQL raw.
from sqlalchemy.engine import URL  # Clase para construir URLs de conexión a la BD (ej: `postgresql://user:pass@host/db`).
from sqlalchemy.orm import Session, sessionmaker  # `Session`: sesión ORM; `sessionmaker`: fábrica de sesiones.

raiz_proyecto = Path(__file__).resolve().parent[2]  # Obtiene ruta base del proyecto subiendo 2 niveles desde el archivo actual
load_dotenv(raiz_proyecto / '.env')  # Carga variables de entorno

# Carga de variables
password = os.environ.get("DB_PASSWORD", "postgres")
username = os.environ.get("DB_USER", "postgres")
host = os.environ.get("DB_HOST", "localhost") 
port = os.environ.get("DB_PORT", "5432")
database = os.environ.get("DB_NAME", "curso_python")

# URL de conexión a la BD
database_url = URL.create(
    "postgresql+psycopg2",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database,
)

engine = create_engine(database_url, pool_pre_ping=True) 
SessionLocal = sessionmaker(bind=engine)

def get_session() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session

def ping(session: Session) -> None: 
    session.execute(text("SELECT 1"))
    
def crear_tablas() -> None: 
    from app.infrastructure.models import Base
    Base.metadata.create_all(bind=engine)