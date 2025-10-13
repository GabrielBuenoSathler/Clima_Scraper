import requests
import psycopg2
from dotenv import load_dotenv
import os
from datetime import datetime


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
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)

    lista_woieds = a
    for cidade in lista_woieds:
        data = connect_api(cidade)
        if data and 'results' in data:
            lista = []
            for key, value in data['results'].items():
                if key != 'forecast':
                    result = insert_no_banco(key, value)
                    if result is not None:
                        lista.append(result)
            print(f"Dados finais para {cidade}: {lista}")

            temp, data_br, cidade_nome = lista

# Converter data de '13/10/2025' para formato do PostgreSQL
            data_pg = datetime.strptime(data_br, "%d/%m/%Y").date()
            my_tuple = (temp, data_pg, cidade_nome)                                                           
            print(my_tuple)                                                                         
            cur.execute("INSERT INTO tempo (maxima, day,nome_cidade ) VALUES (%s, %s,%s)",my_tuple) 

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()



