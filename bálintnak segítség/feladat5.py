import random

lista = []
paros = []
paratlan = []

for i in range (20):
    szam = random.randrange(1,50)
   


for x in lista: 
    if x % 2 == 0: 
        paros.append(x)
    else: 
        paratlan.append(x) 


print('Lista: ' , lista)
print('páros számok: ', paros)
print('páratlanszámok: ',paratlan)


paros.sort()
paratlan.sort()
paratlan.reverse()


print("")
print('páros számok növekvő sorrendbe: ', paros)
print('páratlan számok csökkenő sorrendbe: ', paratlan)
