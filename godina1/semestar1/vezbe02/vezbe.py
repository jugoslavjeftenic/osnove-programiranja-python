import os; os.system("cls")     # brise sadrzaj terminala
zero_fill = 8                   # konstanta vodecih nula

a = 10
b = 3
print(bin(a).zfill(zero_fill))
print(bin(b).zfill(zero_fill))

print("-" * zero_fill)

print(bin(a & b).zfill(zero_fill), end=""); print(" AND")
print(bin(a | b).zfill(zero_fill), end=""); print(" OR")
