import os
import time
from flask import Flask
import psycopg2

app = Flask(__name__)

# Obtener credenciales desde las variables de entorno del docker-compose
DB_HOST = os.environ.get('DB_HOST', 'db_container')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
DB_NAME = os.environ.get('DB_NAME', 'vzeta_db')

def get_db_connection():
    """Intenta conectar a la base de datos con reintentos si aún está iniciando"""
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                dbname=DB_NAME
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    raise Exception("No se pudo conectar a la base de datos PostgreSQL.")

def init_db():
    """Crea la tabla de visitas si no existe"""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS visitas (
            id SERIAL PRIMARY KEY,
            fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()

# Inicializar la tabla al arrancar la app
init_db()

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # 1. Registrar la visita actual
    cur.execute('INSERT INTO visitas DEFAULT VALUES;')
    conn.commit()
    
    # 2. Obtener el contador total
    cur.execute('SELECT COUNT(*) FROM visitas;')
    total_visitas = cur.fetchone()[0]
    
    cur.close()
    conn.close()
    
    return f"<h1>¡Bienvenido a la plataforma de VZeta!</h1><p>Esta es la visita número: <strong>{total_visitas}</strong></p>"

if __name__ == '__main__':
    # Escucha en todas las interfaces en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
