import math
import numpy as np

class Vector2:
    def __init__(self, x:float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        mystr = "Vector2: ("+str(self.x)+","+str(self.y)+")"
        return mystr

    def __str__(self):
        mystr = "Vector2: ("+str(self.x)+","+str(self.y)+")"
        return mystr

    def __eq__(self, other):
        assert (isinstance(other, Vector2))
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        assert (isinstance(other, Vector2))
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        assert (isinstance(other, Vector2))
        return self.Magnitude() < other.Magnitude()

    def __gt__(self, other):
        assert (isinstance(other, Vector2))
        return self.Magnitude() > other.Magnitude()

    def __le__(self, other):
        assert (isinstance(other, Vector2))
        return self.Magnitude() <= other.Magnitude()

    def __ge__(self, other):
        assert (isinstance(other, Vector2))
        return self.Magnitude() >= other.Magnitude()

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __setitem__(self, key, value):
        assert isinstance(key, int)
        assert 0 <= key <= 1
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value

    def __getitem__(self, item):
        assert isinstance(item, int)
        assert 0 <= item <= 1
        if item == 0:
            return self.x
        elif item == 1:
            return self.y

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x+other.x, self.y+other.y)
        elif isinstance(other, (int, float)):
            return Vector2(self.x+other, self.y+other)
        else:
            raise BaseException("Invalid addend for Vector2")

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(other.x-self.x, other.y - self.y)
        elif isinstance(other, (int, float)):
            return Vector2(other - self.x, other-self.y)
        else:
            raise BaseException("Invalid subtracting item for Vector2")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(other*self.x, other*self.y)
        elif isinstance(other, Vector2):
            return other.x*self.x + other.y * self.y

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            assert other!=0
            return Vector2(self.x/other, self.y/other)

    def Magnitude(self):
        return np.sqrt(np.power(self.x,2)+np.power(self.y, 2))

    def Normalize(self, inplace=False):
        if inplace:
            self.x = self.x/self.Magnitude()
            self.y = self.y/self.Magnitude()
        else:
            return Vector2(self.x/self.Magnitude(), self.y/self.Magnitude())

    @staticmethod
    def Distance(a, b):
        assert (isinstance(a, Vector2))
        assert (isinstance(b, Vector2))
        return np.sqrt(np.power((b.x - a.x), 2) + np.power((b.y - a.y), 2))

    @staticmethod
    def Angle(a, b):
        assert (isinstance(a, Vector2))
        assert (isinstance(b, Vector2))
        scalar = a.x * b.x + a.y * b.y
        theta = scalar / (a.Magnitude() * b.Magnitude())
        return np.arccos(theta)

    @staticmethod
    def Cross(a, b):
        assert (isinstance(a, Vector2))
        assert (isinstance(b, Vector2))
        return Vector3(
            abs(a.y * b.z - a.z * b.y),
            abs(a.x * b.z - a.z * b.x)
        )

    @staticmethod
    def Dot(a, b):
        assert (isinstance(a, Vector2))
        assert (isinstance(b, Vector2))
        return a * b

    @staticmethod
    def zeros():
        return Vector2(0, 0)

    @staticmethod
    def ones():
        return Vector2(1, 1)
