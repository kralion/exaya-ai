from db.db_config import supabase

def create_db_boleto(boleto):
    try:
        supabase.table("boletos").insert([boleto])
    except Exception as e:
        print(e)
        return {"error": "Error al insertar el boleto"}
    return {"message": "Boleto insertado correctamente"}

def read_db_boleto(boleto_id):
    try:
        boleto = supabase.table("boletos").select("*").eq("id", boleto_id)
    except Exception as e:
        print(e)
        return {"error": "Error al leer el boleto"}
    return boleto