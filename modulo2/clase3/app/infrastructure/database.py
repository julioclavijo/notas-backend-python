# Base de datos
import os 
from collections.abc import Generator
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.exc import OperationalError # Para manejar errores de conexión a la BD.
from sqlalchemy.orm import Session, sessionmaker

raiz_proyecto = Path(__file__).resolve().parents[1] 
load_dotenv(raiz_proyecto / '.env') 

# Carga de variables
password = os.environ.get("DB_PASSWORD", "postgres")
username = os.environ.get("DB_USER", "postgres")
host = os.environ.get("DB_HOST", "localhost") 
port = os.environ.get("DB_PORT", "5432")
database = os.environ.get("DB_NAME", "database")

# URL de conexión a la BD
database_url = URL.create(
    "postgresql+psycopg",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database,
)

# Motor y ping de la base de datos
engine = create_engine(database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

def get_session() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session

def ping(session: Session) -> None: 
    session.execute(text("SELECT 1"))

def crear_tablas() -> None: 
    from infrastructure.models import Base
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError:
        raise SystemExit(
            "No se pudo conectar a PostgreSQL."
            "Revisa las variables de entorno."
        ) from None
