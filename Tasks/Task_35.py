

def net(n):  
    d = 2
    while n % d != 0:
        d += 1
    return d == n

n = int(input('Enter the number: '))
print(net(n))