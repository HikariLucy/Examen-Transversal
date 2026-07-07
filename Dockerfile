# Imagen base oficial y liviana solicitada por la rúbrica
FROM python:3.12-slim

# Directorio de trabajo interno del contenedor
WORKDIR /app

# Copiar primero los requerimientos para aprovechar la caché de capas de Docker
COPY app/requirements.txt .

# Instalar dependencias del sistema necesarias para compilar psycopg2, 
# instalar los paquetes de pip, y limpiar la basura para mantener la imagen liviana.
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY app/ .

# Exponer el puerto interno de Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

COPY app/ .

# Exponer el puerto interno de Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
