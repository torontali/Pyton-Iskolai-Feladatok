import random

lista = []

for i in range (20):
    szam = random.randrange(1,50)
    lista.append(szam)


for x in lista: 
    min(lista)

print(lista)
print('print lista első legkissebb száma: ',min(lista)) 

lista.remove(min(lista))

print('print lista második legkissebb száma: ',min(lista)) 

lista.remove(min(lista))

print('print lista harmadik legkissebb száma: ',min(lista)) 

lista.remove(min(lista))



    
    

