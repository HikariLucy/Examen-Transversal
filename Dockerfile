# Imagen base oficial y liviana solicitada por la rúbrica
FROM python:3-slim

# Directorio de trabajo interno del contenedor
WORKDIR /app

# Copiar primero los requerimientos para aprovechar la caché de capas de Docker
COPY app/requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY app/ .

# Exponer el puerto interno de Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
