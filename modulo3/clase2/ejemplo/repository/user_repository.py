from sqlalchemy.exc import IntegrityError 
from sqlalchemy.orm import Session

from models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_username(self, username: str) -> User | None:
        return self.db.query(User).filter(User.username == username).first()

    def create(self, username: str, hashed_password: str) -> User:
        user = User(username=username, hashed_password=hashed_password)
        self.db.add(user)
        try:
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            self.db.rollback()
            raise e

    # Obtener usuario por ID
    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first() # Similiar a get_by_username

    # Listar todos los usuarios (revisar)
    def get_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.db.query(User).offset(skip).limit(limit).all() #  devulve segun la paginacion

    # Actualizar un usuario
    def update(self, user_id: int, username: str | None = None, hashed_password: str | None = None) -> User | None:
        # Buscar el usuario con el metodo de get_by_id
        user = self.get_by_id(user_id)
        if not user:
            return None
        # revision de atributos 
        try:
            if username is not None:
                user.username = username
            if hashed_password is not None:
                user.hashed_password = hashed_password

            self.db.commit() # Confirmacion
            self.db.refresh(user)
            return user
        except Exception as e:
            self.db.rollback() # Revierte la transaccion
            raise e

    # Eliminar un usuario
    def delete(self, user_id: int) -> bool:
        # Buscar el usuario de con el metodo definido
        user = self.get_by_id(user_id)
        if not user:
            return False

        self.db.delete(user)
        self.db.commit() # Confirmacion
        return True