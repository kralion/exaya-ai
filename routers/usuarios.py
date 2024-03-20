from pydantic import BaseModel
from ratelimit import limits
from fastapi import APIRouter

from db.usuarios import (
    create_db_usuario,
    read_db_usuario
)

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Not found"}},
)

FIFTEEN_MINUTES = 900

class Usuario(BaseModel):
  username: str
  usuarioDni: str
  foto: str
  sedeDelegacion: str
  telefono: str
  password: str
  nombres: str
  apellidos: str
  sessions: int
  rol: str


@router.get("/{usuario_id}")
@limits(calls=20, period=FIFTEEN_MINUTES)
def read_usuario(usuario_id: str):
    return read_db_usuario(usuario_id)
  
@router.post("/")
@limits(calls=20, period=FIFTEEN_MINUTES)
def create_usuario(usuario: Usuario):
    return create_db_usuario(usuario)
  
  