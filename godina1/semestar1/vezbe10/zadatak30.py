import os; os.system("cls")
from rotiranje import rotiraj_lijevo, rotiraj_desno

moja_lista = [1, 2, 3, 4]

print("Lista nakon rotiranja ulijevo za jedno mjesto:", rotiraj_lijevo(moja_lista))
print("Lista nakon rotiranja udesno za dva mjesta:", rotiraj_desno(moja_lista))
print("Lista nakon rotiranja udesno za dva mjesta:", rotiraj_desno(rotiraj_desno(moja_lista)))
