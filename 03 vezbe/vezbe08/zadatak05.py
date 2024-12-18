import os; os.system("cls")

def count_visible(clients):
    ret_val = [clients[0]]
    for client in clients:
        if ret_val[-1] < client:
            ret_val.append(client)
    return ret_val

print(count_visible([170, 180, 140, 200, 190]))
