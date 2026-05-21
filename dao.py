import mysql.connector


def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="hotelaria",
        use_pure=True
    )
