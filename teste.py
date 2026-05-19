from dao import connection
import time

def banco_atualizado():

    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hospedes")

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados


while True:

    hospedes = banco_atualizado()

    for hospede in hospedes:
        for chave, valor in hospede.items():
            print(f"{chave}: {valor}")
        print("-" * 20)

    time.sleep(5)