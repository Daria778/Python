# Sum of three-digit number

n = int(input('Enter a three-digit number: ' ))
s = 0
if(n >= 100 and n <= 999) : 
    while n > 0 :
        s = s + n % 10 
        n = n // 10
    print(s)
else :
    print('Error')


