#is this a lucky ticket or not?

n = int(input('Enter a six-digit number: ' ))
x = n % 1000
n = n // 1000
sn = 0
sx = 0

while n > 0 :
        sn = sn + n % 10 
        n = n // 10

while x > 0 :
        sx = sx + x % 10 
        x = x // 10   

if sn == sx :
        print('yes')
else :
        print('no')