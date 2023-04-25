n = int(input('Enter the length of the list: '))
a = list()
for i in range(n) :
    z = int(input())
    a.append(z)
print(a)


b = max(a)
c = min(a)


for i in a:
    if b == a[i]:
        a[i] = c
   
print(a)