import os
import httpx
from fastapi import FastAPI, HTTPException, Response

app = FastAPI(title="API Gateway")

DATOS_SERVICE_URL = os.getenv("DATOS_SERVICE_URL", "http://servicio-datos:8001")
RIESGO_SERVICE_URL = os.getenv("RIESGO_SERVICE_URL", "http://servicio-riesgo:8002")

@app.get("/health")
def health_check():
    return {"status": "ok", "servicio": "API Gateway"}

@app.get("/api/v1/datos/{zona_id}")
async def obtener_datos_zona(zona_id: str):
    async with httpx.AsyncClient() as client:
        try:
            respuesta = await client.get(f"{DATOS_SERVICE_URL}/datos/{zona_id}")
            return Response(content=respuesta.content, status_code=respuesta.status_code, media_type="application/json")
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Servicio de Datos no disponible")

@app.post("/api/v1/riesgo/evaluar")
async def evaluar_riesgo(payload: dict):
    async with httpx.AsyncClient() as client:
        try:
            respuesta = await client.post(f"{RIESGO_SERVICE_URL}/evaluar", json=payload)
            return Response(content=respuesta.content, status_code=respuesta.status_code, media_type="application/json")
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Servicio de Riesgo no disponible")