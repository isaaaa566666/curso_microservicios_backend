import os
import psycopg2
import redis
from dotenv import load_dotenv

# Cargar variables de entorno (.env en la raíz del proyecto)
load_dotenv(dotenv_path=".env")

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db_postgres")

REDIS_HOST = os.getenv("REDIS_HOST", "cache_redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

print("🔍 Verificando conexión con PostgreSQL y Redis...\n")
print(f"Usuario PostgreSQL: {POSTGRES_USER}")
print(f"Contraseña PostgreSQL: {POSTGRES_PASSWORD}")
print(f"Base de datos: {POSTGRES_DB}\n")

# --- PostgreSQL ---
try:
    conn = psycopg2.connect(
        host=POSTGRES_HOST,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD
    )
    cur = conn.cursor()
    cur.execute("SET client_encoding TO 'UTF8';")
    cur.execute("SELECT version();")
    version = cur.fetchone()[0]
    print("✅ Conexión a PostgreSQL exitosa")
    print("Versión del servidor:", str(version))
    cur.close()
    conn.close()
except Exception as e:
    print("❌ Error al conectar con PostgreSQL:", repr(e))

# --- Redis ---
try:
    r = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT))
    r.ping()
    print("✅ Conexión a Redis exitosa")
except Exception as e:
    print("❌ Error al conectar con Redis:", e)


