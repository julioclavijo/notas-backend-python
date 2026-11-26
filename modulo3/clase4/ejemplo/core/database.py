from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from core.config import settings

# Arguementos para la conexión a la base de datos
connect_args = {}
if settings.database_url.startswith("postgresql"):
    connect_args["client_encoding"] = "utf-8"

engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inyeccion de dependencias
class Base(DeclarativeBase):
    pass

# Función para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def init_db() -> None:
    import models.user
    Base.metadata.create_all(bind=engine)
    # print("Base de datos inicializada")