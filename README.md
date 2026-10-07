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

## Detener los contenedores

```bash
docker compose down
```
