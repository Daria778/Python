a = str(input('Enter chars: ')).split(' ')
d = dict()
r = list()
n = 0
for i in a :
    if i in d :
        d[i] += 1
        n = d[i]
        r.append(i + '_' + str(n))
    else :
        d[i] = 1
        r.append(i)
print(' '.join(r))


