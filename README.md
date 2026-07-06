# VZeta - Evaluación Final Transversal

Este repositorio contiene la solución para la Evaluación Final Transversal de Tecnologías de Virtualización.

## Estructura
- `app/`: Código fuente de la aplicación Flask en Python y sus dependencias.
- `nginx/`: Configuración del reverse proxy NGINX.
- `Dockerfile`: Definición de la imagen de contenedor para la aplicación.
- `docker-compose.yml`: Orquestación de los contenedores (PostgreSQL, Flask, NGINX).

## Despliegue
Para desplegar este stack de servicios, asegúrate de tener Docker y Docker Compose instalados y ejecuta:
```bash
docker-compose up -d
```
