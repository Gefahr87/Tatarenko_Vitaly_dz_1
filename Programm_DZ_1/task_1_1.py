
d = 0
h = 0
m = 0
s = 0
duration = []
for i in range(int(input('Enter amount enters:'))):
    duration.append(int(input('Enter amount seconds:')))
    d = duration[i] // 86400
    h = (duration[i] % 86400) // 3600
    m = ((duration[i] % 86400) % 3600) // 60
    s = ((duration[i] % 86400) % 3600) % 60
    if duration[i] < 60:
        print(str(s), ' сек ')
    elif duration[i] < 3600:
        print(str(m), ' мин ',str(s), ' сек ')
    elif duration[i] < 86400:
        print(str(h), ' час ',str(m), ' мин ',str(s), ' сек ')
    else:
        print(str(d),' дн ',str(h), ' час ',str(m), ' мин ',str(s), ' сек ')
