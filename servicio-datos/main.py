from fastapi import FastAPI, HTTPException

app = FastAPI(title="Servicio de Datos")

BASE_DATOS_ZONAS = {
    "valparaiso-centro": {
        "zona_id": "valparaiso-centro",
        "temperatura_c": 29.5,
        "humedad_porcentaje": 28.0,
        "viento_kmh": 32.0,
        "vegetacion": "Matorral seco",
        "incendios_historicos": 6
    },
    "vina-del-mar": {
        "zona_id": "vina-del-mar",
        "temperatura_c": 21.0,
        "humedad_porcentaje": 65.0,
        "viento_kmh": 14.0,
        "vegetacion": "Pino y eucalipto",
        "incendios_historicos": 2
    }
}

@app.get("/datos/{zona_id}")
def obtener_datos_zona(zona_id: str):
    if zona_id not in BASE_DATOS_ZONAS:
        raise HTTPException(status_code=404, detail="Zona no encontrada")
    return BASE_DATOS_ZONAS[zona_id]