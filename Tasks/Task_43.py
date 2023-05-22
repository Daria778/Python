n = int(input('Enter the length of the first list: '))
a = list()
for i in range(n) :
    z = int(input())
    a.append(z)
print(a)

s = 0
for i in range(len(a)):
    for j in a[i + 1 :]:
        if a[i] == j:
            s += 1


print(s)