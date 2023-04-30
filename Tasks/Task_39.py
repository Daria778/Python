n = int(input('Enter the length of the first list: '))
a = list()
for i in range(n) :
    z = int(input())
    a.append(z)
print(a)

n1 = int(input('Enter the length of the second list: '))
a1 = list()
for i in range(n1) :
    z = int(input())
    a1.append(z)

print(a1)

b = list()

for i in range(len(a)):
    if a[i] not in a1:
        b.append(a[i])
    
print(b)