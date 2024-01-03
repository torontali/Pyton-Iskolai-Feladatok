#számok
numbers = [32 ,5, 12, 8, 3, 75, 2, 15]

#páros lista
even =[]

#páratlan lista
odd = []

#berakja a páros számokat a 'páros' listába
for odd_number in numbers:
    if odd_number % 2 != 0:
       odd.append(odd_number)

#berakja a páratlan számokat a 'páratlan ' listába
for even_number in numbers:
    if even_number % 2 == 0:
        even.append(even_number)

print('páros lista: ', even)
print('páratlan lista: ',odd)