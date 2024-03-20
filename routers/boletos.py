from ratelimit import limits
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from db.usuarios import (
    create_db_usuario,
    read_db_usuario
)

FIFTEEN_MINUTES = 900

router = APIRouter(
    prefix="/boletos",
    tags=["boletos"],
    responses={404: {"description": "Not found"}},
)

class Boleto(BaseModel):
    asiento: int
    pasajeroDni: str
    codigo: str
    fechaRegistro: datetime
    equipaje: Optional[str]
    id: str
    precio: int
    reservado: bool
    telefonoCliente: str
    viaje: str
    viajeId: str

@router.get("/{boleto_id}")
@limits(calls=20, period=FIFTEEN_MINUTES)
def read_boleto(boleto_id: int, boleto: Boleto):
    return {"boleto_id": boleto_id, "boleto": boleto}

@router.post("/")
@limits(calls=20, period=FIFTEEN_MINUTES)
def create_boleto(boleto_id: int, boleto: Boleto):
    return {"boleto_id": boleto_id, "boleto": boleto}
