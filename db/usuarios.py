from db.db_config import supabase
from pydantic import BaseModel
from fastapi import NotFoundError

class Usuario(BaseModel):
  id : str
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

class UsuarioCreate (BaseModel):
    username: str
    usuarioDni: str
    foto: str
    sedeDelegacion: str
    telefono: str
    password: str
    nombres: str
    apellidos: str
    rol: str
    


# data, count = supabaseClient.table('usuarios').insert({"id": "assdu23921351", "username": "exaya", "password" : "Exaya_2024", "foto" : "https://cdn-icons-png.flaticon.com/128/6873/6873405.png", "apellidos" : "INC" , "nombres": "Exaya", "usuarioDni": "71780367", "sedeDelegacion": "Huancayo", "rol": "GUEST", "telefono":"914019629"}).execute()

def read_db_usuario(usuario_id: str):
    try :
        usuario = supabase.table('usuarios').select("*").eq('id', usuario_id).execute()
    except Exception as e:
        print(e)
        return {"error": "Error al leer el usuario"}
    return usuario

  
def create_db_usuario(usuario: UsuarioCreate):
    try:
        usuario = supabase.table('usuarios').insert([usuario]).execute()
    except Exception as e:
        print(e)
        return {"error": "Error al insertar el usuario"}
    return usuario


  
