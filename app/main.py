import json    # Arreglos del input json (ordenar texto)
import hashlib # Libreria para realizar el calculo el hash md5

from fastapi import FastAPI, Request, Header #los campos necesarios para mas adelante 
from pydantic import BaseModel, Field 
from typing import Dict, Any

app = FastAPI(title="Urbetrack MD5 challenge", description="API REST para validar MD5 sobre un JSON normalizado", version="1.0.3",)

class NormalizarRequest(BaseModel):
    payload: Dict[str, Any] = Field(..., description="JSON normalizado a validar")
    md5: str = Field(..., description="Valor MD5 esperado")

#                                 Endpoint 01 - HEALTH
@app.get("/health")
def health_check():
    return {"status": "ok"}

#                                 Endpoint 02 - JSON
@app.post("/validar_mensaje")
def validate_message(request: NormalizarRequest):
    normalized_json = json.dumps(
        request.payload,
        sort_keys=True,
        separators=(",", ":"),
    )
    calculated_md5 = hashlib.md5(normalized_json.encode("utf-8")).hexdigest()

    if calculated_md5 != request.md5.lower():
        return {"Valido": False, "MD5": calculated_md5}        
    return {"Valido": True, "MD5": calculated_md5}

    


# HASK OK: 8ddf45693d4185b95732d263fade0be2
# "payload": {"empresa":"UrbeTrack","name":"Paulo"}
# otro hash OK segun como se encripte: calculo_md5 487dd71db6ca994eafa617b7911406ae



# Para probar:
# curl -X POST http://localhost:8080/validar_md5 -H "Content-Type: application/json" -H "x-md5: 487dd71db6ca994eafa617b7911406ae" -d '{"payload": {"empresa":"UrbeTrack", "name":"Paulo"}}'



