from dao import connection

RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
YELLOW = "\033[93m"
GRAY   = "\033[90m"

def select():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hospedes")
    dados = cursor.fetchall()
    headers = [desc[0].upper() for desc in cursor.description]
    cursor.close()
    conn.close()
    return dados, headers

dados, headers = select()

W = [len(h) for h in headers]
for hospede in dados:
    for i, val in enumerate(hospede):
        W[i] = max(W[i], len(str(val)))

VB = "║"

def hline(left, mid, right):
    return left + mid.join("═" * (w + 2) for w in W) + right

def row(cols, color=WHITE):
    cells = f" {VB} ".join(f"{color}{str(v):<{W[i]}}{RESET}" for i, v in enumerate(cols))
    return f"{VB} {cells} {VB}"

print()
print(f"  {CYAN}{BOLD}LISTA DE HÓSPEDES{RESET}  {GRAY}{DIM}{len(dados)} registro(s){RESET}")
print()
print("  " + hline("╔", "╦", "╗"))
print("  " + row(headers, color=f"{YELLOW}{BOLD}"))
print("  " + hline("╠", "╬", "╣"))

for i, hospede in enumerate(dados):
    cor = WHITE if i % 2 == 0 else GRAY
    print("  " + row(hospede, color=cor))

print("  " + hline("╚", "╩", "╝"))
print()