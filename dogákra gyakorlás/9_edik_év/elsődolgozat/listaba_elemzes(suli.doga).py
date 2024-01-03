'''keresztnevek = []
nev = None

while nev != '':
    nev = input('adj meg 1 keresztnevet ami legalább 3 betből áll')
    if nev != '' and len(nev) >=3:
        keresztnevek.append(nev)

for i in keresztnevek:
    print('nev:',i,'harmadik betű',i[2])


novenyek = ['ibolya','tulipán','ibolya','rózsa','szegfű']

beolvas=None
beolvas= input('Adj meg 1 növényy nevet: ')
db = 0

for noveny in novenyek:
    if noveny == beolvas:
        db += 1

if db != 0 :
    print('enyiszer szerepelt már benne: ' , db)
else:
    print('nemszerepelt benne') 
    novenyek.append(beolvas)

print((',').join (novenyek))
print('')




szamok = list ()
import random
for i in range(1,21):
    szam = random.randrange(15,45)
    if szam % 3 == 0 :
        szamok.append(szam)

print(szamok)
'''

 
   
