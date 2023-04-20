print('Enter the sequence of numbers: ')
r = list()
s = 0
while True:
    a = int(input())

    r.append(a)
    if a == 0:
        break
s = max(r)
print(r)
print(s, "- max")