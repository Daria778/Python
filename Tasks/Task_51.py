a = [2, 4, 6, 1]

def same_by(characteristic, objects):
    return len(list(filter(characteristic, objects))) == 0

if same_by(lambda x: x % 2, a):
    print('same')
else:
    print('different')
