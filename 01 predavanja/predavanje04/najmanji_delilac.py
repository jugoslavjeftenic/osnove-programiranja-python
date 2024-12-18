import os; os.system("cls")

broj_za_proveru = 23
najmanji_delilac = 0
for delilac in range(2, broj_za_proveru):
    if broj_za_proveru % delilac == 0:
        najmanji_delilac = delilac
        break

if najmanji_delilac > 0:
    print("Najmanji delilac je: ", najmanji_delilac)
else:
    print("Broj je prost i deljiv je sa 1 ili samim sobom.")
