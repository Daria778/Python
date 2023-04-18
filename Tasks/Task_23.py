a = [0, -1, 5, 2, 3]
s = 0
#если i + 1 больше чем i, то  s += 1

for i in range(len(a)) :
    if a[i] > a[i - 1] :
        s += 1
    else :
        s += 0
print(s)