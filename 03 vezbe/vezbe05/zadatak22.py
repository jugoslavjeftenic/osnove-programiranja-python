import os; os.system("cls")

# Funkcija: prosti_u_intervalu Napisati funkciju prosti_u_intervalu koja prima dva prirodna broja
# m i n i ispisuje sve proste brojeve u intervalu [m, n].

def da_li_je_prost(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prosti_u_intervalu(m, n):
    for i in range(m, n + 1):
        if da_li_je_prost(i):
            print(i, "je prost broj.")

prosti_u_intervalu(1, 20)
