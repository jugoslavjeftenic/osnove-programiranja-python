def rotiraj_lijevo(lista):
    if not lista: return []
    return lista[1:] + [lista[0]]

def rotiraj_desno(lista):
    if not lista: return []
    return lista[-1:] + lista[:-1]
