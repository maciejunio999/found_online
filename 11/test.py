slownik = {"min_rating": 2300, "victory_status": "draw"}
#print(slownik['max_rating'])

lista = [x for x in range(0, 10)]

for i in range(0, 16):
    if i not in lista:
        lista.append(i)

print(lista)