import os; os.system("cls")

# Napisati funkciju palindrom koja kao parametar prima string i
# proverava da li je taj string palindrom (čita se isto sa obe strane).
# Funkcija vraća True ako jeste, u suprotnom False.

def is_palindrom(text):
    reversed_text = ""
    reverse_counter = len(text)

    while reverse_counter > 0:
        reversed_text += text[reverse_counter - 1]
        reverse_counter -= 1
    
    return text == reversed_text

print(is_palindrom("ratar"))
