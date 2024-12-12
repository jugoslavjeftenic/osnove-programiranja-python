import os; os.system("cls")

def dnevnik(students):
    try:
        student = int(input("Unesite redni broj ucenika: "))
        print("Ime trazenog studenta:", students[student-1])
    except ValueError:
        print("Niste uneli ispravan broj.")
    except IndexError:
        print(f"Redni broj studenta mora biti izmedju 1 i {len(students)}.")

dnevnik(["Marko", "Ana", "Maja", "Iva"])
