def Fib(n):
    if n in [0, 1]:
        return 1
    return Fib(n - 1) + Fib(n - 2)
    

count = int(input("Enter tne number: "))
print(Fib(count))
