a = list()
x = int(input('Enter the length of list: '))
y = int(input('Enter the number you want to find: '))
for i in range(x) :
    z = int(input())
    a.append(z)
print(a)

s = 0

for i in range(len(a)) :
    if a[i] == y :
        s += 1
print(s)
