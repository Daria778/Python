a = list()
x = int(input('Enter the length of list: '))
y = int(input('Enter the nearest number you want to find: '))
for i in range(x) :
    z = int(input())
    a.append(z)
print(a)
d = 0
p = a[0]
mind = a[0]


for i in range(len(a)) :
        if y > a[i] :
             d = y - a[i]
             if d <= mind :
              mind = d
              p = a[i]
        if y == a[i] :
            p = y
            mind = 0
            break
        if y < a[i] :
            d = a[i] - y
            if d <= mind :
                 mind = d
                 p = a[i]
print(mind)

print(p)
   
