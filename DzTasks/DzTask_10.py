n = int(input('Enter the amount of numbers: '))
s = 0
v = 0
d = 0
for i in range(0,n) :
    x = int(input())
    if x == 1 :
        s += 1
    elif x == 0 :
        v += 1
    else :
         break
        
if x != 0 and x!= 1 :
    print('Error')
    
elif s > v :
    d = v
    print(d, 'times')
elif s < v :
    d = s
    print(d, 'times')
elif s == v :

    print(s)
    