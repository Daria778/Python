n = int(input('Enter the length of the list: '))
a = list()

for i in range(n) :
    z = int(input())
    a.append(z)
print(a)

b = int(input('Enter the lower restriction: '))
c = int(input('Enter the upper restriction: '))

d = list()

for i in range(len(a)):
    if a[i] >= b and a[i] <= c:
        d.append(i)
    else:
        pass
print(d)

