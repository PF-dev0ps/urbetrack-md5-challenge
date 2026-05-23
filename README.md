# * Urbetrack MD5 Challenge *

## Overview

This project implements a REST API to validate MD5 hashes generated from a JSON input.

The solution uses FastAPI and includes:

- REST API with Swagger/OpenAPI documentation
- Dockerized applicacion
- Nginx reverse proxy
- Docker Compose orquestration
- Bash scripts requested
- GitHub Actions CI workflow
- Check Health



## 🚀 Inicio rápido



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