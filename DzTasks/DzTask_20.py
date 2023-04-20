s = str(input('Enter the word: ')).upper()
print(s)

a = {1 : "AEIOULNSTR", 2 : "DG", 3 : "BCMP", 4 : "FHVWY", 5 : "K", 8 : "JX", 10 : "QZ"} 
z = "AEIOULNSTRDGBCMPFHVWYKJXQZ"

count = 0

b = {1 : "АВЕИНОРСТ", 2 : "ДКЛМПУ", 3 : "БГЁЬЯ", 4 : "ЙЫ", 5 : "ЖЗХЦЧ", 8 : "ШЭЮ", 10 : "ФЩЪ" }
y = "АВЕИНОРСТДКЛМПУБГЁЬЯЙЫЖЗХЦЧШЭЮФЩЪ"

if s[0] in z:
    for i in s:
        for k in a:
            if i in a[k]:
                count += k
    print(count)
elif s[0] in y:
    for i in s:
        for k in b:
            if i in b[k]:
                count += k
    print(count)
else:
    print('Error')



