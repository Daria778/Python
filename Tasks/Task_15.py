n = int(input('Enter the amount of numbers: '))
max = 0
min = 30000

for i in range(0,n,1) :
    x = int(input())
    if x > max :
        max = x
    if x < min :
        min = x
print(min, "- min", max, "- max")

