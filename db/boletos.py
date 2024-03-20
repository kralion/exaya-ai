from db.db_config import supabase
from pydantic import BaseModel
from datetime import datetime

class Boleto(BaseModel):
    id : str
    asiento: int
    pasajeroDni: str
    codigo: str
    fechaRegistro: datetime
    equipaje: str
    precio: int
    reservado: bool
    telefonoCliente: str
    viaje: str
    viajeId: str
    
class BoletoCreate(BaseModel):
    asiento: int
    pasajeroDni: str
    codigo: str
    fechaRegistro: datetime
    equipaje: str
    precio: int
    reservado: bool
    telefonoCliente: str
    viaje: str
    viajeId: str
    
# TODO: Add Session parameter for allowing only authenticated users to create a Boleto
def create_db_boletos(boleto: BoletoCreate):
    try :
        supabase.table('boletos').insert([boleto]).execute()
    except Exception as e:
        print(e)
        return {"error": "Error al insertar el boleto"}
    return {"message": "Boleto insertado correctamente", }

def read_db_boleto(boleto_id: str):
    try :
        boleto = supabase.table('boletos').select("*").eq('id', boleto_id).execute()
    except Exception as e:
        print(e)
        return {"error": "Error al leer el boleto"}
    return boleto