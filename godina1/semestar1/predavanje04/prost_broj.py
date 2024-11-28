import os; os.system("cls")

broj_za_proveru = 8
jeste_prost_broj = True
for delilac in range(2, broj_za_proveru):
    if broj_za_proveru % delilac == 0:
        jeste_prost_broj = False
        break

if jeste_prost_broj is not True:
    print("Broj nije prost.")
else:
    print("Broj je prost.")
