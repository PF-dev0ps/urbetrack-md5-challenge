import json
import hashlib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="Urbetrack MD5 challenge",
    description="API REST para validar MD5 sobre un JSON normalizado",
    version="1.0.3",    
)

class ValidateMD5Request(BaseModel):
    payload: dict = Field(..., description="JSON a validar")
    md5: str = Field(..., description="Valor MD5 esperado") 

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/validate-md5")
def validate_md5(request: ValidateMD5Request):
    normalized_json = json.dumps(request.payload,sort_keys=True,separators=(',', ':'),ensure_ascii=False,)
    calculated_md5 = hashlib.md5(normalized_json.encode('utf-8')).hexdigest()

    if calculated_md5 != request.md5.lower():
        raise HTTPException(status_code=422, detail={"Error:":"MD5 mismatch","Expected": request.md5, "Calculated": calculated_md5,},)

    return {"Valido": True, "MD5": calculated_md5,}
