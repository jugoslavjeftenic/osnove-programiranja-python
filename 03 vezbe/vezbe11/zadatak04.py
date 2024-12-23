from os import system; system("cls")

products = [
    {"product":"kafa", "quantity":10, "price":400},
    {"product":"sladoled", "quantity":5, "price":100},
    {"product":"keks", "quantity":8, "price":200}
]

print("Cijena kafe je: {} kredita.".format(products[0]["price"]))

if products[1]["quantity"] > products[2]["quantity"]:
    print("Na stanju ima vise sladoleda.")
elif products[1]["quantity"] < products[2]["quantity"]:
    print("Na stanju ima vise keksa.")
else:
    print("Na stanju je podjednaka kolicina sladoleda i keksa.")

most_expensive = max(products, key=lambda p: p["price"])
print(f"Najskuplji artikal je {most_expensive["product"]}.")
