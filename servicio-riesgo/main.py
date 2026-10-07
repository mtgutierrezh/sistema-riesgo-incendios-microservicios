from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Servicio de Riesgo")

class SolicitudEvaluacion(BaseModel):
    temperatura_c: float
    humedad_porcentaje: float
    viento_kmh: float
    vegetacion: str
    incendios_historicos: int

@app.post("/evaluar")
def evaluar_riesgo(datos: SolicitudEvaluacion):
    puntuacion = 0

    if datos.temperatura_c > 25.0:
        puntuacion += 1
    if datos.humedad_porcentaje < 40.0:
        puntuacion += 1
    if datos.viento_kmh > 20.0:
        puntuacion += 1
    if datos.incendios_historicos > 3:
        puntuacion += 1

    if puntuacion >= 3:
        nivel = "Alto"
    elif puntuacion == 2:
        nivel = "Medio"
    else:
        nivel = "Bajo"

    return {
        "nivel_riesgo": nivel,
        "puntuacion_calculada": puntuacion
    }