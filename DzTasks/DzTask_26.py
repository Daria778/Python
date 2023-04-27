a = int(input('Enter'))
b = int(input('Enter'))



def degree(a, b):
    if b == 1:
        return a
    return a * degree(a, b - 1)

print(degree(a, b))

