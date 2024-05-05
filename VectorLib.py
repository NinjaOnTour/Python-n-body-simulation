import math

def Distance(pos0, pos1):
    return math.sqrt((pos0.X-pos1.X)**2 + (pos0.Y-pos1.Y)**2 + (pos0.Z-pos1.Z)**2)
    

class Vector3:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def GetInfo(self):
        return "(" + str(round(self.X, 2)) + ", " + str(round(self.Y, 2)) + ", " + str(round(self.Z, 2)) + ")"

    def Magnitude(self):
        return math.sqrt(self.X**2 + self.Y**2 + self.Z**2)
    
    def Normalize(self):
        return self / self.Magnitude()
    
    def __truediv__(self, other):
        return Vector3(self.X / other, self.Y / other, self.Z / other)
    
    def __add__(self, other):
        return Vector3(self.X + other.X, self.Y + other.Y, self.Z + other.Z)
    
    def __sub__(self, other):
        return Vector3(self.X - other.X, self.Y - other.Y, self.Z - other.Z)
    
    def __mul__(self, other): 
        return Vector3(self.X * other, self.Y * other, self.Z * other)
    
    def __neg__(self):
        return Vector3(-self.X, -self.Y, -self.Z)