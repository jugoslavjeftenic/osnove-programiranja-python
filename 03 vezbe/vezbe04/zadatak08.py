import os; os.system("cls")

primalac = "Univerzitet Singidunum, Danijelova 32, Beograd"

def uplata(iznos, broj_racuna = "265-1780310001129-52", svrha_uplate = "Uplata skolarine"):
    # student = {}
    student = {"ime":"Pera", "prezime":"Peric", "adresa":"Perina 12", "broj_indeksa":"2024000123"}
    # student["ime"] = input("Upisite ime: ")
    # student["prezime"] = input("Upisite prezime: ")
    # student["adresa"] = input("Upisite adresu: ")
    # student["broj_indeksa"] = input("Upisite broj indeksa: ")

    print("Uplatnica")
    print("Uplatilac:", student["ime"], student["prezime"], student["adresa"], student["broj_indeksa"])
    print("Svrha uplate:", svrha_uplate)
    print("Iznos:", iznos)
    print("Primalac:", primalac)
    print("Racun primaoca:", broj_racuna)

uplata(25000.00)
