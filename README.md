# * Urbetrack MD5 Challenge *

## Overview

This project implements a REST API to validate at the same time if a MD5 hash is OK with the JSON input recieved.

The solution uses FastAPI and includes:

- REST API with Swagger/OpenAPI documentation
- Dockerized applicacion
- Nginx reverse proxy
- Docker Compose orquestration
- Bash scripts requested
- GitHub Actions CI workflow
- Check Health

<img src="screenshots/ubt-04.png" width="20%">

### Instalación y ejecución

```bash
# 1. Clonar el repositorio
  git clone PF-dev0ps/urbetrack-md5-challenge.git
  cd urbetrack-md5-challenge

# 2. Levantar el servicio
  ./scripts/start.sh

# 3. URL que expone el servicio:
  http://localhost:8080/docs

# 4. Bajar el servicio:
  ./scripts/stop.sh

```
Desde la web podemos validar el mensaje

<img src="screenshots/ubt-03.png" width="20%">

Si quisieras probar en consola:

```bash
# 1. Para verificar que funciona:
     curl http://localhost:8080/health

# 2. Si quisieras para probar el endpoint de validar y no el Health desde consola
  enviar este comando con el mensaje & llave incluidos:

  curl -X POST http://localhost:8080/validar_mensaje \
  -H "Content-Type: application/json" \
  -d '{
      "payload": {"empresa":"UrbeTrack", "name":"Paulo"},
      "md5": "8ddf45693d4185b95732d263fade0be2"}'
```


---

# Architecture

Client
    |
    v
  Nginx Reverse Proxy
                   |
                   v
                FastAPI Application

Componentes:

- FastAPI handles the REST API and Swagger/OpenAPI generation.
- Nginx works as reverse proxy.
- Docker Compose orchestrates the containers.
- GitHub Actions validates itself, build and do the execution automatically.

##Screenshots

<p align="center">
  <img src="screenshots/ubt-01.png" width="20%">
  <img src="screenshots/ubt-02.png" width="20%">
  <img src="screenshots/ubt-03.png" width="20%">
  <img src="screenshots/ubt-04.png" width="20%">
</p>

# comprobaciones con curl en consola:

://urbetrack-md5-challenge2$ curl -X POST localhost:8080/validar_mensaje -H "Content-Type: application/json" -d '{"payload": {"empresa":"UrbeTrack", "name":"Paulo"},"md5": "487dd71db6ca994eafa617b7911406ae"}'
{"Valido":false,"MD5":"8ddf45693d4185b95732d263fade0be2"}


://urbetrack-md5-challenge2$ curl -X POST localhost:8080/validar_mensaje -H "Content-Type: application/json" -d '{"payload": {"empresa":"UrbeTrack", "name":"Paulo"},"md5": "8ddf45693d4185b95732d263fade0be2"}'
{"Valido":true,"MD5":"8ddf45693d4185b95732d263fade0be2"}
