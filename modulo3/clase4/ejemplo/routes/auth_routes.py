from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.auth_service import (
    CredencialInvalida,  
    UsuarioYaExiste,
    iniciar_sesion,
    registrar_usuario
)
from core.database import get_db
from schemas.user_schemas import LoginResponse, UserCreate, UserLogin, UserResponse

router = APIRouter(tags=["Autenticacion"]) # tag esta en desuso

@router.post("/register", response_model=UserResponse, status_code=201, summary="Registrar nuevo usuario")
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    try:
        return registrar_usuario(data, db)
    except UsuarioYaExiste:
        raise HTTPException(status_code=400,detaiL="Usuario ya existe")

@router.post("/login", response_model=LoginResponse, status_code=200, summary="Inciar sesión")
def login_user(data: UserLogin, db: Session = Depends(get_db)):
    try:
        user, token = iniciar_sesion(data, db)
    except CredencialInvalida:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return LoginResponse(
        access_token=token,
        token_type="bearer",
        user=UserResponse.model_validate(user),
    )

