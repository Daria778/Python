n = int(input('Enter the length of the first list: '))
a = list()
for i in range(n) :
    z = int(input())
    a.append(z)
print(a)

s = 0
i = 0
while i != len(a):
    if a[i] == a[0]:
        i += 2
        continue
    elif a[i] == a[-1]:
        break
    elif a[i] > a[i - 1] and a[i] > a[i + 1]:
        s += 1
    i += 1
print(s)