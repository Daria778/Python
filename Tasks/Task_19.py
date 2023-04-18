list_1 = [1, 2, 3, 4, 5]
k = int(input())

if k > 0 :
    for i in range(k) :
        list_1.insert(0, list_1.pop())
else :   
    k *= -1
    for i in range(k) :
        list_1.append(list_1.pop(0))
    
print(list_1)

