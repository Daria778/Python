a = int(input('Enter the first member of the arithmetic progression: '))
d = int(input('Enter the difference of the arithmetic progression: '))
n = int(input('Enter the quantity of the arithmetic progression: '))

c = list()

for i in range(1, n + 1):
    c.append(a)
    a += d
print(c)
