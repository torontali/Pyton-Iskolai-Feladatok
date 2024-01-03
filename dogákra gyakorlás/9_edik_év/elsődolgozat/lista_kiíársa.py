keresztnevek = []

nev = input('adj meg 1 nevet')

while nev != '':
    nev = input('adj meg 1 nevet')
    if nev != '':
        keresztnevek.append(nev)

for i in keresztnevek:
    print('a keresztnevek 3. bütje: ', i[2], ', a keresztnevek: ', i)
