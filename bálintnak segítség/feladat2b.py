import random

lista = []

for i in range (20):
    szam = random.randrange(1,50)
    lista.append(szam)

bekeres = int(input("adj mehg 1 számot: "))

closest_value = min(lista, key=lambda x: abs(x - bekeres))

print('lista: ',lista)

lista.remove(closest_value)

closest_value2 = min(lista, key=lambda x: abs(x - bekeres))

print('Első legközelebbi: ',closest_value)
print('Második legközelebbi: ',closest_value2)