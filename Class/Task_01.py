import random
import statistics

class Human:
    def __init__(self, age, name, surname, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades
    def __str__(self) -> str:
        return f"{self.name, self.surname, self.age}"
    
    def greet(self):
        return f"Hi, my name is {self.name} {self.surname}, and i am {self.age} years old"
    
    def __repr__(self) -> str:
        return self.name
    
    def avg(self):
        return statistics.mean(self.grades)
    

hum = Human(36, "Dante", "Sparda", [])
#print(hum.greet())
hum1 = Human(37, "Vergil", "Sparda", [])
hum2 = Human(40, "Sekiro", "Shinobi", [])
hum3 = Human(75, "Issin", "Asina", [])
hum4 = Human(15, "Kuro", "divine heir", [])

lst = [hum, hum1, hum2, hum3, hum4]
for i in lst:
    i.grades = [random.randint(1, 5) for j in range(6)]

lst.sort(key= lambda x: x.avg())

print(lst)

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def cords(self):
        return [a.x, a.y, b.x, b.y]
    
    def place(self):
        return (b.x - a.x)*(a.y - b.y)
    
    def per(self):
        return ((b.x - a.x)* 2) + ((a.y - b.y)*2)

    def has_point(self, point):
        if point.x < max(a.x, b.x) and point.y < max(a.y,b.y) and point.x > min(a.x, b.x) and point.y > min(a.y, b.y):
            return True
        else:
            return False
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
a = Point(1, 10)
b = Point(10, 1)
smth = Rectangle(a, b)
x = Point(0, 9)
print(smth.place())
print(smth.per())
print(smth.has_point(x))