a = int(input('Enter: '))
b = int(input('Enter: '))

def sum(a, b):
    if b == 0:
        return a
    return 1 + sum(a, b - 1)
print(sum(a, b))