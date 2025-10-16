import psycopg2
from psycopg2 import OperationalError

# Connection parameters
params = {
    "host": "localhost",
    "port": 5432,
    "dbname": "banking",
    "user": "postgres",
    "password": "B@z1ngaa!"
}

try:
    # Attempt to connect to PostgreSQL
    conn = psycopg2.connect(**params)
    print("✅ Connection to PostgreSQL successful!")
    conn.close()
except OperationalError as e:
    print(f"❌ Connection failed: {e}")