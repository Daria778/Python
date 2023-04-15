a = int(input('Enter the number: '))
l = int(input('Enter the low for number: ' ))
s = 0
n = 2
f = 0

if a > 1 and l >= a:
    while True:
         s += (n - 1) + (n - 2)
         f += 1

         if s == a :
              print(s, f + 1) # count from 0
              break
         
else :
     print('Error')
