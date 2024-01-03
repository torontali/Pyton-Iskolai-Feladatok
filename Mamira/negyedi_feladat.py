lista = []

találat = False


import random

for i in range (1,21):
    szam = random.randrange(-10,10)
    lista.append(szam)

print("A feltételnek megfelelő elem(ek): ")
for x in range(0, len(lista)-1, 1): 
    
    if x > 0  and x < len(lista)-2:
        osszeg = lista[x-1]+lista[x+1]
        
        if osszeg == lista[x]:
            print(x+1,". elem:",lista[x],"(szomszédos elemek értékei:",lista[x-1],", ",lista[x+1],")")
            találat = True
           
if találat == False:
    print("nincs ilyen elem")
            
            