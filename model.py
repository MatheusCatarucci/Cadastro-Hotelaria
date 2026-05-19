from dao import connection


# ──────────────────────────────────────────
# HÓSPEDES
# ──────────────────────────────────────────
def consulta_hospede(id):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            select * from hospedes
            where id = %s
            """

    cursor.execute(query, (id,))
    retorno = cursor.fetchone()

    cursor.close()
    conn.close()

    return retorno


def add_hospede(nome, email, telefone, cpf):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            insert into hospedes (nome, email, telefone, cpf)
            values (%s, %s, %s, %s)
            """

    cursor.execute(query, (nome.capitalize(), email, telefone, cpf))
    id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return id


def consulta_hospedes():
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    query = """
            select * from hospedes
            """

    cursor.execute(query)
    retorno = cursor.fetchall()
    cursor.close()
    conn.close()
    return retorno