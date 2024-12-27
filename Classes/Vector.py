import math

class Vector2:
    x = 0
    y = 0

    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y
    def __add__(self, a):
        return Vector2(self.x + a.x, self.y + a.y)
    def __sub__(self, a):
        return Vector2(self.x - a.x, self.y - a.y)
    def __mul__(self, a):
        if type(a) == float or type(a) == int:
            return Vector2(self.x * a, self.y * a)
        else:             
            return Vector2(self.x * a.x, self.y * a.y)
    def __div__(self, a):
        return Vector2(self.x / a.x, self.y / a.y)
    def mag(self):
        return (self.x**2 + self.y**2)**0.5
    def dot(self, OtherVector):
        return self.x * OtherVector.x + self.y * OtherVector.y
    def angle(self):
        return math.atan(self.y / self.x)
    
        