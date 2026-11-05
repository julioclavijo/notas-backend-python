from pathlib import Path
from urllib.parse import quote_plus
from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

APP_DIR = Path(__file__).resolve().parents[1]

class Settings(BaseSettings):
    # Configuración de la aplicación cargada desde variables de entorno
    
    model_config = SettingsConfigDict(
        env_file=APP_DIR / ".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    db_user: str = "postgres"
    db_pass: str = "postgres"
    db_host: str = "localhost"
    db_port: str = "5432"
    db_name: str = "db ejemplo"

    cors_origins: list[str] = [
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ]

    @property
    def database_url(self) -> str:
        user = quote_plus(self.db_user)
        password = quote_plus(self.db_pass)
        return f"postgresql+psycopg2://{user}:{password}@{self.db_host}:{self.db_port}/{self.db_name}"


def load_settings() -> Settings: 
    try:
        return Settings()  
    except ValidationError as exc:
        raise RuntimeError("Falta SECRET_KEY en el archivo .env") from exc

settings = load_settings()