
def report(n):
    a = input()
    if n == 1:
        return a 
    return report(n - 1) + a
n = int(input("Enter the number: "))
print(report(n))