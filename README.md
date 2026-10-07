# Microservicios de Riesgo de Incendios

Sistema compuesto por un API Gateway, un servicio de datos y un servicio de evaluación de riesgo.

## Requisitos

- Docker Desktop en Windows.
- Docker Engine y Docker Compose en Linux.

## Ejecución

Desde la carpeta del proyecto, ejecutar:

### Windows PowerShell

```powershell
docker compose up --build -d
docker compose ps
```

### Linux

```bash
docker compose up --build -d
docker compose ps
```

El API Gateway queda disponible en `http://localhost:8000`.

Servicios directos:

- Datos: `http://localhost:8001`
- Riesgo: `http://localhost:8002`

Documentación interactiva:

- `http://localhost:8000/docs`
- `http://localhost:8001/docs`
- `http://localhost:8002/docs`

## Pruebas

### Docker (estado general)

```powershell
docker compose ps
docker compose logs --tail=20
docker compose logs api-gateway
docker compose logs servicio-datos
docker compose logs servicio-riesgo
```

### API Gateway (`:8000`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/health"
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/datos/valparaiso-centro"
```

```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/datos/valparaiso-centro
```

### Servicio de Datos (`:8001`)

```powershell
Invoke-RestMethod -Uri "http://localhost:8001/datos/valparaiso-centro"
Invoke-RestMethod -Uri "http://localhost:8001/datos/vina-del-mar"
```

```bash
curl http://localhost:8001/datos/valparaiso-centro
curl http://localhost:8001/datos/vina-del-mar
```

### Servicio de Riesgo (`:8002`)

```powershell
$body = @{
  temperatura_c       = 29.5
  humedad_porcentaje  = 28.0
  viento_kmh          = 32.0
  vegetacion          = "Matorral seco"
  incendios_historicos = 6
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8002/evaluar" -Method Post -ContentType "application/json" -Body $body
```

```bash
curl -X POST http://localhost:8002/evaluar \
  -H "Content-Type: application/json" \
  -d '{"temperatura_c":29.5,"humedad_porcentaje":28.0,"viento_kmh":32.0,"vegetacion":"Matorral seco","incendios_historicos":6}'
```

### Prueba end-to-end (a través del Gateway)

```powershell
$body = @{
  temperatura_c       = 29.5
  humedad_porcentaje  = 28.0
  viento_kmh          = 32.0
  vegetacion          = "Matorral seco"
  incendios_historicos = 6
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/riesgo/evaluar" -Method Post -ContentType "application/json" -Body $body
```

```bash
curl -X POST http://localhost:8000/api/v1/riesgo/evaluar \
  -H "Content-Type: application/json" \
  -d '{"temperatura_c":29.5,"humedad_porcentaje":28.0,"viento_kmh":32.0,"vegetacion":"Matorral seco","incendios_historicos":6}'
```

## Detener los contenedores

```bash
docker compose down
```