import requests
import psycopg2
from dotenv import load_dotenv
import os

def connect_api(cidade):
    url = f"https://api.hgbrasil.com/weather?woeid={cidade}"
    r = requests.get(url)
    if r.status_code == 200:
        print("API funcionando")
        return r.json()
    else:
        print("API com problemas")
        return None

def insert_no_banco(key, value):
    if key == 'temp':
        print(f"TEMPERATURA: {value}")
    elif key == 'date':
        print(f"DIA: {value}")
    elif key == 'city_name':
        print(f"CIDADE: {value}")
    else:
        return None
    return value

def main():
    lista = []
    cidade = 455825  # Rio de Janeiro
    data = connect_api(cidade)

    if data and 'results' in data:
        for key, value in data['results'].items():
            if key != 'forecast':
                result = insert_no_banco(key, value)
                if result is not None:
                    lista.append(result)

    

if __name__ == "__main__":
    main()

load_dotenv()

host = os.getenv("host")
port =  os.getenv("port")
database = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")
print(host)
print(port)
print(user)
print(password)

conn_params = {
    "host": host,
    "port": port,
    "database": database,
    "user": user,
    "password": password
}




# Connect to PostgreSQL
try:
    conn = psycopg2.connect(**conn_params)
    print("Connected to the database!")

   # Create a cursor to execute SQL
    cur = conn.cursor()

    # Example query
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print("Database version:", db_version)

    # Clean up
    
    

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)

cur.execute("SELECT * FROM tempo")
row = cur.fetchone()
print(row)
                            

cur.close()
