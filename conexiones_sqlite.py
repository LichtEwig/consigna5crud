import sqlite3 as sq3

# CONEXION
def get_connetion():
    global database
    database = 'netflix_oscar.db'
    conn = sq3.connect(database)
    return conn

# DESCONEXION
def close_connetion():
    cursor.close()
    conn.close()
      
# CONSULTA
def read_database():
    is_conn = False
    try:
        global conn
        global cursor
        conn = get_connetion()
        cursor = conn.cursor()
        cursor.execute('SELECT sqlite_version()') # para la versión de SQL es @@version
        db_version = cursor.fetchone()
    except (Exception, sq3.Error) as error:
        print(f'Houston tenemos problemas: {error}')
    else:
        print(f'Estamos conectados en la BBDD {database}... ')
        print(f'Con la versión de SQLite: {db_version}')
        is_conn = True
    finally:
        if is_conn:
            close_connetion()
            print('Se ha cerrado la conexión')

read_database()
