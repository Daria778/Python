n = int(input('enter the amount of days: ' ))

# 50 -10 -45 10 20 -30
#2

p = 0
m = 0
for i in range(0, n, 1) :
    x = int(input())
    if x > 0 :
     p += 1
    else :
     if p > m :
       m = p
       p = 0
if p > m :
  m = p
   

print(m)
