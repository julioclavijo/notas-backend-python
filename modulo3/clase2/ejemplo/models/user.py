from sqlalchemy import Column, DateTime, Integer, String 
from sqlalchemy.orm import validates 
from sqlalchemy.sql import func

from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, comment="ID del usuario")
    username = Column(
        String(50),
        unique=True,
        index=True,
        nullable=False,  
        comment="Nombre de usuario único"  
    )
    hashed_password = Column(
        String(255),
        nullable=False,  
        comment="Contraseña hasheada del usuario"  
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),  
        comment="Fecha y hora de creación del usuario" 
    )
    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
        comment="Fecha y hora de la última actualización"  
    )
    @validates('username')
    def validate_username(self, key, username: str) -> str:
        if not username:
            raise ValueError("El nombre de usuario no puede estar vacío")

        if len(username) < 3:
            raise ValueError("El nombre de usuario debe tener como mínimo 3 caracteres")

        if len(username) > 50:
            raise ValueError("El nombre de usuario no puede exceder de 50 caracteres")

        if not username.replace('_', '').replace('-', '').isalnum():
            raise ValueError("El nombre de usuario solo puede contener letras, números, guiones y guiones bajos")

        return username.strip().lower()

    @validates('hashed_password')
    def validate_hashed_password(self, key, hashed_password: str) -> str:
        if not hashed_password:
            raise ValueError("La contraseña hasheada no puede estar vacía")
        return hashed_password

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}')>"