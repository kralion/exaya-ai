from ratelimit import limits
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
    responses={404: {"description": "Not found"}},
)

FIFTEEN_MINUTES = 900



@router.get("/{usuario_id}")
@limits(calls=20, period=FIFTEEN_MINUTES)
def read_usuario(usuario_id: int):
    usuario = read_db_usuario(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


  
@router.post("/")
@limits(calls=20, period=FIFTEEN_MINUTES)
def create_usuario(usuario: UsuarioCreate):
    try:
        usuario = create_db_usuario(usuario)
        return usuario
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(
            e, "Error al crear el usuario"
        ))
        

  