lista = []

import random

print('ebben a listába 20 random szám közül a 3-ommal oszthatokat fogja kiírni')

for i in range (1,21):
    szam = random.randrange(15,45)
    if szam % 3 ==0:
        lista.append(szam)

print(lista, 'enyi elemből áll ez a lista: ',len(lista))

