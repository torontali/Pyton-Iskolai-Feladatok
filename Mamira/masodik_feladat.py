lista = []
sorszam = []

szamlalo = 1
kezdo_eretek = 1
vegso_eretek =21

import random

for i in range (kezdo_eretek,vegso_eretek):
    szam = random.randrange(-10,10)
    lista.append(szam)
    sorszam.append(szamlalo)
    szamlalo += 1
    
'''print("Az alap számok listája: ")
for x in range(0,vegso_eretek-1):
    print(sorszam[x],".","elem: ",lista[x])
'''

lista.reverse()
sorszam.reverse()

print("A lsita fordított sorrende: ")
for x in range(0,vegso_eretek-1):
    print(sorszam[x],".","elem: ",lista[x])

print("lista fordított sorendje: ")