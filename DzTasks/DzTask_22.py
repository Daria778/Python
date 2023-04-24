#Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств

n = int(input('Enter the length of the first set: '))
a = set()
m = int(input('Enter the length og the second set: '))
b = set()

print('Enter the values for the first set:')
for i in range(n) :
    z = int(input())
    a.add(z)
print(a)
print('Enter the values for the second set:')
for i in range(m) :
    z = int(input())
    b.add(z)
print(b)

l = a & b
l = list(l)


for i in range(len(l) - 1):
    if l[i] > l[i + 1]:
        temp = l[i]
        l[i] = l[i + 1]
        l[i + 1] = temp
print(l)   

