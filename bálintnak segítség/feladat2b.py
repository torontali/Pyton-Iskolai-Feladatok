lista = []


import random

for i in range (20):
    szam = random.randrange(1,50)
    lista.append(szam)

bekeres = int(input("adj mehg 1 számot: "))

closest_value = min(lista, key=lambda x: abs(x - bekeres))

print(lista)
print("Az első legközelebb álló szám:" ,closest_value[0], closest_value[1])


















