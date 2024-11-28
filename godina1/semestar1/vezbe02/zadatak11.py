import os; os.system("cls")     # brise sadrzaj terminala

studijski_program = input("Unesite studijski program: ")
if studijski_program.upper() == "SII" or studijski_program.upper() == "IT":
    print("Na ovom smeru se rade tri testa. Test inteligencije, opste informisanosti i informaticki test. Radi se i intervu.")
elif studijski_program.upper() == "PE":
    print("Na ovom smeru se radi intervju na srpskom jeziku.")
elif studijski_program.upper() == "TH":
    print("Na ovom smeru se radi intervju na engleskom jeziku.")
