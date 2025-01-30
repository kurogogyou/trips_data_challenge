import psycopg2

# Database Configuration
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Pa$$1234",
    "port": "5432",
    "host": "localhost"
}

def get_connection():
    """Establish and return a database connection."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True
        return conn
    except psycopg2.Error as e:
        print("Error connecting to database:", e)
        return None
