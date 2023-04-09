# Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input('Enter a three-digit number: ' ))
s = 0
if(n >= 100 and n <= 999) : 
    while n > 0 :
        s = s + n % 10 
        n = n // 10
    print(s)
else :
    print('Error')


