orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# a = list(filter(lambda x: True if x[0] != x[1] else False, orbits))
# print(a)
a = list(map(lambda x: 3.14 * x[0] * x [1] if x[0] != x[1] else -1, orbits))
# b = list(map(lambda y: 3.14 * y[0] * y[1], a))
v = max(a)
for i in range(len(a)):
    if a[i] == v:
        print(orbits[i])
        break
    else:
        pass