import psycopg2

def create_table():
    conn =  psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")# 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL )")  #3.- Crear un enunciado SQL
    conn.commit()#4.- Commit changes to conection
    conn.close()#5.- Cerrar la conexion

def append_values(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")# 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)" , (item,quantity,price))  #3.- Crear un enunciado SQL
    conn.commit()#4.- Commit changes to conection
    conn.close()#5.- Cerrar la conexion

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") # 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()#5.- Cerrar la conexion
    return rows

def delete_values(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") # 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("DELETE FROM store WHERE item=%s",(item,))  #3.- Crear un enunciado SQL
    conn.commit()#4.- Commit changes to conection
    conn.close()#5.- Cerrar la conexion

def update_value(quantity,price,item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'") # 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))  #3.- Crear un enunciado SQL
    conn.commit()#4.- Commit changes to conection
    conn.close()#5.- Cerrar la conexion

create_table()
# append_values('Otro',10,8.5)
delete_values('Otro')
print(view())
