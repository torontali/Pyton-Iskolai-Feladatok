lista = []

elso_szam = 1
utolso_szam = 21


import random

for i in range (elso_szam,utolso_szam):
    szam = random.randrange(1,50)
    lista.append(szam)




bekeres = int(input("adj meg 1 számot 1 és 50 között számot: "))

print(lista)

for x in range (0, utolso_szam-1 ,1):
    if bekeres > x :
        print(lista[-1], bekeres)

