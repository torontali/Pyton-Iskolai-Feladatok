lista = []

elso_szam = 1
utolso_szam = 21
tavolsag1 = 51
tavolsag2 = 52


import random

for i in range (elso_szam,utolso_szam):
    szam = random.randrange(1,50)
    lista.append(szam)




bekeres = int(input("adj meg 1 számot 1 és 50 között számot: "))

for x in lista:
    if x > bekeres: 
       tavolsag = x - bekeres
       if tavolsag < tavolsag1: 
         tavolsag1 = tavolsag
    elif x < bekeres:
       tavolsag = bekeres - x
       if tavolsag1> tavolsag:
            tavolsag1 = tavolsag
    else: 
        '''egyeb esetben egyenlő'''
        tavolsag1 = 0
    '''if tavolsag1 > tavolsag2:
        tarolo= tavolsag2
        tavolsag2= tavolsag1
        tavolsag1= tarolo
'''

print("A lista: " ,lista)
print( "A bekért szám: ", bekeres)
print("tavolsag1: ", tavolsag1)
print("tavolsag2: ",tavolsag2)