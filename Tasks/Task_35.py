def net(n):  
    for i in range(2, int(pow(n, 0.5))):
        if n % i == 0:
            return False
        return True

n = int(input('Enter the number: '))
print(net(n))