n = int(input())

def summa(n):
    if n == 0:
        return n
    return summa(a = int(input(), n - 1))

summa(n)