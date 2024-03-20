from .limiter import limiter
from fastapi import APIRouter, HTTPException

from db.usuarios import (
    create_db_usuario,
    read_db_usuario,
    UsuarioCreate,
    Usuario
)

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "El usuario no fue encontrado en la base de datos"}},
)

FIFTEEN_MINUTES = 900



@router.get("/{usuario_id}")
@limiter.limit("1/second")
def read_usuario(usuario_id: int):
    usuario = read_db_usuario(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return Usuario(**usuario.__dict__)


  
@router.post("/")
@limiter.limit("1/second")
def create_usuario(usuario: UsuarioCreate):
    try:
        usuario = create_db_usuario(usuario)
        return usuario
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(
            e, "Error al crear el usuario"
        ))
        

  