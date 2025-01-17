from math import tan

class Vector2:
    X = 0
    Y = 0

    def __init__(self, X = 0 , Y = 0):
        self.X = X
        self.Y = Y
    def __add__(self, a):
        return Vector2(self.X + a.X, self.Y + a.Y)
    def __sub__(self, a):
        return Vector2(self.X - a.X, self.Y - a.Y)
    def __mul__(self, a):
        if type(a) == float or type(a) == int:
            return Vector2(self.X * a, self.Y * a)
        else:             
            return Vector2(self.X * a.X, self.Y * a.Y)
    def __div__(self, a):
        return Vector2(self.X / a.X, self.Y / a.Y)
    def mag(self):
        return (self.X**2 + self.Y**2)**0.5
    def dot(self, OtherVector):
        return self.X * OtherVector.X + self.Y * OtherVector.Y
    def angle(self):
        return math.atan(self.Y / self.X)
    
        