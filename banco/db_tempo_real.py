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


ultimo_resultado = None

while True:

    hospedes = banco_atualizado()

    # Só imprime se houver mudança
    if hospedes != ultimo_resultado:

        print("\n=== BANCO ATUALIZADO ===\n")

        for hospede in hospedes:
            for chave, valor in hospede.items():
                print(f"{chave}: {valor}")

            print("-" * 20)

        ultimo_resultado = hospedes

    time.sleep(5)