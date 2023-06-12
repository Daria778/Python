import statistics
import math
from typing import Any
class Dragon:
    def __init__(self, height, fire_danger, color) -> None:
        self.height = height
        self.fire_danger = fire_danger
        self.color = color

    def __repr__(self):
        return f"{self.height, self.fire_danger, self.color}"

    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.fire_danger} and color {self.color}"
    
    def __add__(self, other):
            a = self.fire_danger
            if other.fire_danger > a:
                a = other.fire_danger    
            b = math.floor((self.height + other.height) / 2)
            c = self.color
            if other.color < c:
                 c = other.color
            kol = Dragon(a, b, c)
            return kol
    
    def __sub__(self, other):
         a = self.height // other
         b = self.height - a
         x = self.fire_danger % other
         c = self.fire_danger + x
         z = self.color
         lok = Dragon(b, c, z)
         return lok

    def change_color(self, color):
         self.color = color
         return self.color
    
    def __call__(self, string):
         return string * self.fire_danger
          
    def __eq__(self, other):
         return self.height == other.height and self.fire_danger == other.fire_danger and self.color == other.color              
    def __lt__(self, other):
         return self.height < other.height and self.fire_danger < other.fire_danger and self.color < other.color
    def __gt__(self, other):
         return self.height > other.height and self.fire_danger > other.fire_danger and self.color > other.color
dr = Dragon(69, 11, "brown")
dr1 = Dragon(5, 16, "black")
dr2 = dr + dr1
#print(dr.change_color("black"))
print(dr - 2)
print(dr, dr1, dr2, sep="\n")
print(dr("Welcome")) 
print(dr > dr1, dr != dr1, dr == dr1)