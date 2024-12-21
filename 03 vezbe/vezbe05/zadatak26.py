from os import system; system("cls")

def prebroj_recenice():
    # input_text = input("Unesite tekst sa vise recenica: ")
    # input_text = "U koliko sati je kolokvijum? U 16 sati."
    input_text = "Dan je bio neobičan. Kiša je odjednom stala! Zar je moguće? Pogledao je u nebo - pojavila se duga! Prelepa! Šta li donosi taj trenutak?"
    counter = 0
    counter += input_text.count(".")
    counter += input_text.count("!")
    counter += input_text.count("?")
    
    return counter

print("Broj recenica:", prebroj_recenice())
