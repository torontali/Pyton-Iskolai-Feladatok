novenyek = ['ibolya','rózsa','ibolya']
noveny = None
bekeres = input('Adj meg 1 növényt: ')

db = 0

for noveny in novenyek:
    if noveny == bekeres:
        db += 1

if db !=0 :
     print('ez a novény már szerepel a listában', db, '-szer')
else:
    print('ez a növény nem szerepel a listában')
    novenyek.append(bekeres)
    print((',').join(novenyek))

