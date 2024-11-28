import os; os.system("cls")     # brise sadrzaj terminala

import datetime as dv
datum = dv.datetime.now()

print(datum)

print(f"{datum:%a}")
print(f"{datum:%A}")
print(f"{datum:%d}")
print(f"{datum:%m}")
print(f"{datum:%Y}")
print(f"{datum:%w}")
print(f"{datum:%b}")
print(f"{datum:%j}")
print(f"{datum:%B}")

print(f"{datum:%H}")
print(f"{datum:%I}")
print(f"{datum:%M}")
print(f"{datum:%S}")

print(f"{datum:%d.%m.%Y.}")
print(f"{datum:%d:%m:%Y}")
