import random
import string
import mysql.connector

def connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='hotelaria'
    )

conn = connection()

# Aumenta o limite do pacote para o máximo permitido (~1GB)
cursor = conn.cursor()
cursor.execute("SET GLOBAL max_allowed_packet = 1073741824")
cursor.close()

cursor = conn.cursor()

query = """
INSERT INTO hospedes (nome, email, telefone, cpf)
VALUES (%s, %s, %s, %s)
"""

def gerar_nome():
    nomes = ["Matheus", "João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Carlos", "Fernanda", "Rafael"]
    sobrenomes = ["Silva", "Souza", "Oliveira", "Costa", "Pereira", "Rodrigues", "Almeida"]
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

def gerar_email(nome):
    usuario = nome.lower().replace(" ", ".")
    dominios = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com"]
    return f"{usuario}{random.randint(1,99999999)}@{random.choice(dominios)}"

def gerar_telefone():
    return f"119{random.randint(10000000, 99999999)}"

def gerar_cpf():
    return ''.join(random.choices(string.digits, k=11))

dados = []

for _ in range(100000):
    nome = gerar_nome()
    email = gerar_email(nome)
    telefone = gerar_telefone()
    cpf = gerar_cpf()

    dados.append((nome, email, telefone, cpf))

cursor.executemany(query, dados)

conn.commit()

print("100 mil dados inseridos com sucesso!")

cursor.close()
conn.close()