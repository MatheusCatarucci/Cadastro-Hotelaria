import mysql.connector

def connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='hotelaria_2'
    )

while True:
    conn = connection()
    cursor = conn.cursor()

    query = """
        SELECT * FROM hospedes
    """
    cursor.execute(query)
    retorno = cursor.fetchall()
    print(retorno)
    cursor.close()
    conn.close()