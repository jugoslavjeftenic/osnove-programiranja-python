import os; os.system("cls")     # brise sadrzaj terminala

ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")
ime_i_prezime = ime + prezime
trazena_osoba = "Marko Markovic"

if    ime.upper() in trazena_osoba.upper() and prezime.upper() in trazena_osoba.upper(): print("Pogodili ste trazenu osobu.")
else: print ("Niste pogodili trazenu osobu.")
