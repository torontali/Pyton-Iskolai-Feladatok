t1 = ['31','28','31','30','31','31','30','31','30','31','30','31']
t2 = ['január','február','március','április','május','június','július','algusztus','szeptember','október','November','december']

t3= []


if len(t1) == len(t2):
    for number in range(len(t1)):
        t3.append(t2[number]+' '+ t1[number]+',')

    print(t3)
else:
    print('nem egyekzik meg a 2 lista száma')




