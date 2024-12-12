import math
from functools import total_ordering
@total_ordering
class Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    
    def __abs__(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __mul__(self, other):
        return Vector(self.x*other,self.y*other,self.z*other)
    
    def __rmul__(self, other):
        return Vector(self.x*other,self.y*other,self.z*other)
    
    def __gt__(self, other):
        return abs(self) > abs(other)
    
    def __bool__(self):
        return abs(self) > 0
    
    def __getitem__(self, item):
        if item.lower() in ["x","y","z"]:
            return eval(f"self.{item.lower()}")
        else:
            return NotImplemented
