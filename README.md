# VZeta - Evaluación Final Transversal

Este repositorio contiene la solución para la Evaluación Final Transversal de Tecnologías de Virtualización.

## 🛠️ Estructura del Proyecto
* **app/**: Código fuente de la aplicación Flask en Python y sus dependencias.
* **nginx/**: Configuración del reverse proxy NGINX.
* **Dockerfile**: Definición de la imagen de contenedor estable basada en `python:3.12-slim`.
* **docker-compose.yml**: Orquestación del stack (PostgreSQL, Flask, NGINX).

---

## 🚀 Evidencias de Despliegue e Indicadores de Logro

### 1. Instalación de Herramientas y Entorno (IE 2.3.1)
Se instaló correctamente Docker Engine y Docker Compose en la instancia EC2 de AWS Learner Lab.
![Docker Instalado](evidencias/Docker Instalado.png)

### 2. Construcción de Imagen Personalizada (IE 2.3.1)
Se modificó el `Dockerfile` para utilizar una base estable de Python 3.12, resolviendo problemas de dependencias de compilación con `psycopg2-binary`. La imagen fue construida localmente con éxito:
```bash
docker build -t myapp:latest .
![Imágenes Construidas](evidencias/docker images.png)

3. Orquestación y Funcionamiento del Stack (IE 3.2.3 / IE 3.3.1)
El stack completo se levantó de forma aislada en segundo plano compartiendo la red interna y asegurando la persistencia mediante volúmenes para PostgreSQL. Las consultas de los clientes responden con éxito por el puerto 80 a través del Reverse Proxy de NGINX:

Bash
docker compose up -d
curl http://localhost/
![Incremento de Visitas y Persistencia](evidencias/curl 2.png)

4. Auditoría e Inspección Técnica (IE 3.3.2)
Se utilizaron herramientas de inspección avanzada para validar el montaje del volumen persistente de la base de datos, los direccionamientos IP y el estado de salud de la red del ecosistema:

Bash
docker inspect db_container --format='{{json .Mounts}}'
![Inspect Base de Datos](evidencias/inspect db_container.png)
![Inspect Red y Servicios](evidencias/inspect examen transversal.png)
![Inspect Status de la App](evidencias/Inspect myaapp.png)

5. Control del Ciclo de Vida y Métricas (IE 2.3.3)
Se ejecutaron y documentaron comandos administrativos para auditar registros de tráfico (logs), estadísticas de consumo en tiempo real (stats), así como comandos operacionales de ciclo de vida (restart, stop, rename, rm, rmi), solventando bloqueos de entorno mediante la señalización de procesos (kill):
![Logs y Estadísticas](evidencias/Docker logs.png)

Despliegue Rápido
Para volver a desplegar este entorno de forma automática, ejecuta:

Bash
docker compose up -d
