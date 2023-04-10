#Сколько журавликов сделал каждый ребенок

n = int(input('Enter the S number: ' ))
if n % 6 == 0 :
    x = 1
    x = n // (2 * x + 4 * x)
    print('Peter -', x, 'Kate -', x * 4, 'Sergey -', x)
else :
    print('Error')
