import os; os.system("cls")     # brise sadrzaj terminala

studijski_program = input("Unesite studijski program: ")
match studijski_program.upper():
    case "SII": print("Na ovom smeru se rade tri testa. Test inteligencije, opste informisanosti i informaticki test. Radi se i intervu.")
    case "IT":  print("Na ovom smeru se rade tri testa. Test inteligencije, opste informisanosti i informaticki test. Radi se i intervu.")
    case "PE":  print("Na ovom smeru se radi intervju na srpskom jeziku.")
    case "TH":  print("Na ovom smeru se radi intervju na engleskom jeziku.")
