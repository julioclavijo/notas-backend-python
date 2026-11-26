from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from auth.jwt import crear_token
from auth.password import hashear_password, verificar_password
from models.user import User
from repository.user_repository import UserRepository
from schemas.user_schemas import UserCreate, UserLogin

class UsuarioYaExiste(Exception): 
    pass
class CredencialInvalida(Exception):
    pass

def registrar_usuario(db: Session, data: UserLogin) -> User:
    repository = UserRepository(db)
    if repository.get_by_username(data.username): 
        raise UsuarioYaExiste

    hashed = hashear_password(data.password) 
    try: 
        return repository.create(data.username, hashed)
    except IntegrityError as exc: 
        raise UsuarioYaExiste from exc


def iniciar_sesion(db: Session, data: UserLogin) -> tuple[User, str]:
    user = UserRepository(db).get_by_username(data.username)
    if user is None or not verificar_password(data.password, user.hashed_password):
        raise CredencialInvalida

    return user, crear_token({"sub": user.username})
    