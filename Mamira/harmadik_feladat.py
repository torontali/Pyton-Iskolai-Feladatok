lista = []

import random

for i in range (1,21):
    szam = random.randrange(-10,10)
    lista.append(szam)


x =  sum(lista)
print("---------------------------------")
print("A lista számmainak összege: ",x)


if x % 3 == 0: 
    print("A szám osztható 3-al")
    print("---------------------------------")
else: 
    print("A szám nem oszthato 3-al")
    print("---------------------------------")