from ratelimit import limits
from fastapi import APIRouter, HTTPException
from db.boletos import (
   create_db_boletos,
   read_db_boleto,
   BoletoCreate,
   Boleto
)

FIFTEEN_MINUTES = 900

router = APIRouter(
    prefix="/boletos",
    tags=["boletos"],
    responses={404: {"description": "El boleto no fue encontrado en la base de datos"}},
)



@router.get("/{boleto_id}")
@limits(calls=20, period=FIFTEEN_MINUTES)
def read_boleto(boleto_id: int, boleto: Boleto):
    try :
        boleto = read_db_boleto(boleto_id)
        if boleto is None:
            raise HTTPException(status_code=404, detail="Boleto no encontrado")
        return Boleto(**boleto.__dict__)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/")
@limits(calls=20, period=FIFTEEN_MINUTES)
def create_boleto(boleto: BoletoCreate):
    try:
        create_db_boletos(boleto)
        return {"message": "Boleto insertado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
