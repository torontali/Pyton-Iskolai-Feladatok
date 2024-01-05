import random

lista = []
eredmeny = []

for i in range (20):
    szam = random.randrange(1,50)
    lista.append(szam)


lista.sort()

for x in range(0, len(lista)-1, 1):
    if lista[x] == lista[x+1]:
        eredmeny.append(lista[x])

print(lista)
print(eredmeny)