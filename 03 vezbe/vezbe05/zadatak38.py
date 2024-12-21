from os import system; system("cls")

sum = 0
for n in range(10, 100):
    if n % 3 == 0 and n % 4 != 0 and str(n)[0] != str(n)[1]:
        sum += n

print("Zbir brojeva koji su deljivi sa 3, nisu deljivi sa 4 i imaju razlicite cifre je:", sum)
