import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db") # 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL )")  #3.- Crear un enunciado SQL
    conn.commit()#4.- Commit changes to conection
    conn.close()#5.- Cerrar la conexion

def append_values(item,quantity,price):
    conn = sqlite3.connect("lite.db") # 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))  #3.- Crear un enunciado SQL
    conn.commit()#4.- Commit changes to conection
    conn.close()#5.- Cerrar la conexion

def view():
    conn = sqlite3.connect("lite.db") # 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()#5.- Cerrar la conexion
    return rows

def delete_values(item):
    conn = sqlite3.connect("lite.db") # 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("DELETE FROM store WHERE item=?",(item,))  #3.- Crear un enunciado SQL
    conn.commit()#4.- Commit changes to conection
    conn.close()#5.- Cerrar la conexion

def update_value(quantity,price,item):
    conn = sqlite3.connect("lite.db") # 1.- Abrir la conexion a la DB
    cur = conn.cursor()  #2.- Crear un cursor
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))  #3.- Crear un enunciado SQL
    conn.commit()#4.- Commit changes to conection
    conn.close()#5.- Cerrar la conexion

delete_values('Wine Glass')
print(view())
