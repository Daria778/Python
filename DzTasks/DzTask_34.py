a = ('пара-ра-рам рам-пам-папам па-ра-па-да')
print(a)
d = a.count('а')
def vinny(operation, objects):
    return len(list(filter(operation, objects))) == 0
n = len(a.split(' '))
if vinny(lambda x: d % n, a):
    print('Парам пам-пам')
else:
    print('Пам парам')
