n = int(input('Enter the number: ' ))
n1 = 1
if n == 0 :
    print(1)
else :
    while n > 0 :
        n1*= n
        n -= 1
    print(n1)