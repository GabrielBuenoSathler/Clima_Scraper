import psycopg2

conn_params = {
    "host": "localhost",
    "port": 5432,
    "database": "clima",
    "user": "clima123",
    "password": "clima123"
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

cur.execute("CREATE TABLE tempo  (id serial PRIMARY KEY, day date, maxima int,minima int);")
                            

conn.commit()
cur.close()


