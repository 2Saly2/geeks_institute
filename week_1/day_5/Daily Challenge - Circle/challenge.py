import math
from functools import total_ordering

@total_ordering
class Circle:
    def __init__(self,radius=None , diameter=None):
        if (radius is None)==(diameter is None):
            raise ValueError("Provide exactly one argument: radius OR diameter")
        if diameter is not None:
            radius =diameter/2
        if radius < 0:
            raise ValueError("the radius must be positive")
        self._radius = float(radius)
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
        if value < 0 :
            raise ValueError("the radius must be positif")
        self._radius= float(value)
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @diameter.setter
    def diameter(self,value):
        if value < 0:
            raise ValueError("diameter must be positif")
        self._radius= float(value) / 2
    
    @property
    def area(self):
        return math.pi *self._radius **2
    

    def __repr__(self):
        return f"Circle(radius ={self._radius})"
    
    def __str__(self):
        return f"Circle(radius={self._radius} , diameter={self.diameter}, area={self.area:.3f})"
    
    def __add__(self,other):
        if not isinstance(other ,Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return math.isclose(self.radius , other.radius)
    
    def __lt__(self,other):
        if not isinstance(other,Circle):
            return NotImplemented
        return self.radius < other.radius
    
if __name__ == "__main__":
    c1 = Circle(radius=3)
    c2 = Circle(diameter=8)

    print(c1)
    print(c2)

    c1.diameter = 10
    print(c1.radius)

    c3 = c1 + c2
    print(c3)

    print(c1 < c2)
    print(c1 == Circle(radius=5))

    Circles = [c2 ,c3,c1]
    print(sorted(Circles))
    
     
