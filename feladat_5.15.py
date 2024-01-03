#nevek
names =['Jean','Maximilien','Brigitte','Soina','Jean-Pierre','Sandra']

#
less_than_6 = []

more_or_equal_6 = []

for i in names:
    if len(i) <=5: 
        less_than_6.append(i)
    else:
        more_or_equal_6.append(i)

print('kisebb számok mint 6', less_than_6)
print('nagyobb vagy egyenlő számú nevek mint 6:', more_or_equal_6)
