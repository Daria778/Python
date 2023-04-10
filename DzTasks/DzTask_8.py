#chocolate

m = int(input('Enter m:' ))
n = int(input('Enter n:' ))
k = int(input('Enter k pices:' ))
print(m*n)
print((m*n)%2)
if (m * n) % 2 == 0 and (k % 2 == 0 or k % 3 == 0):
    
    print('yes')
else :
    print('no')