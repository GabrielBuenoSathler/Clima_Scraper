import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
port = os.getenv("port")
database = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")

print(host, port, user, password)

conn_params = {
    "host": host,
    "port": port,
    "database": database,
    "user": user,
    "password": password
}

try:
    conn = psycopg2.connect(**conn_params)
    print("Connected to the database!")

    cur = conn.cursor()
    cur.execute("SELECT woeid FROM woeids ");
    row = cur.fetchall()
    a = [x[0] for x in row]
    print(len(a))
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)

