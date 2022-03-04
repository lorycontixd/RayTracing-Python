import math
import numpy as np


class Vector3:
    def __init__(self, x: float, y: float, z: float):
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        assert isinstance(z, (int, float))
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        mystr = "Vector3: (" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
        return mystr

    def __str__(self):
        mystr = "Vector3: (" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
        return mystr

    def __eq__(self, other):
        assert (isinstance(other, Vector3))
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        assert (isinstance(other, Vector3))
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __lt__(self, other):
        assert (isinstance(other, Vector3))
        return self.Magnitude() < other.Magnitude()

    def __gt__(self, other):
        assert (isinstance(other, Vector3))
        return self.Magnitude() > other.Magnitude()

    def __le__(self, other):
        assert (isinstance(other, Vector3))
        return self.Magnitude() <= other.Magnitude()

    def __ge__(self, other):
        assert (isinstance(other, Vector3))
        return self.Magnitude() >= other.Magnitude()

    def __bool__(self):
        return self.x != 0 or self.y != 0 or self.z != 0

    def __setitem__(self, key, value):
        assert isinstance(key, int)
        assert 0 <= key <= 2
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            self.z = value

    def __getitem__(self, item):
        assert isinstance(item, int)
        assert 0 <= item <= 2
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            return self.z

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            raise BaseException("Invalid addend for Vector3")

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(other.x - self.x, other.y - self.y, other.z - self.z)
        elif isinstance(other, (int, float)):
            return Vector3(other - self.x, other - self.y, other - self.z)
        else:
            raise BaseException("Invalid subtracting item for Vector3")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(other * self.x, other * self.y, other * self.z)
        elif isinstance(other, Vector3):
            return other.x * self.x + other.y * self.y + other.z * self.z

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            assert other != 0
            return Vector3(self.x / other, self.y / other, self.z / other)


    def Print(self):
        pass

    def Magnitude(self):
        return np.sqrt(np.power(self.x, 2) + np.power(self.y, 2) + np.power(self.z, 2))

    def Normalize(self, inplace=False):
        if inplace:
            self.x = self.x / self.Magnitude()
            self.y = self.y / self.Magnitude()
            self.z = self.z / self.Magnitude()
        else:
            return Vector3(self.x / self.Magnitude(), self.y / self.Magnitude(), self.z / self.Magnitude())

    @staticmethod
    def Distance(a, b):
        assert (isinstance(a, Vector3))
        assert (isinstance(b, Vector3))
        return np.sqrt(np.power((b.x - a.x), 2) + np.power((b.y - a.y), 2) + np.power((b.z - a.z), 2))

    @staticmethod
    def Angle(a, b):
        assert (isinstance(a, Vector3))
        assert (isinstance(b, Vector3))
        scalar = a.x * b.x + a.y * b.y + a.z * b.z
        theta = scalar / (a.Magnitude() * b.Magnitude())
        return np.arccos(theta)

    @staticmethod
    def Cross(a, b):
        assert (isinstance(a, Vector3))
        assert (isinstance(b, Vector3))
        return Vector3(
            abs(a.y * b.z - a.z * b.y),
            abs(a.x * b.z - a.z * b.x),
            abs(a.x * b.y - a.y * b.x)
        )

    @staticmethod
    def Dot(a, b):
        assert (isinstance(a, Vector3))
        assert (isinstance(b, Vector3))
        return a * b

    @staticmethod
    def FromList(l: list):
        assert len(l) == 3
        return Vector3(l[0], l[1], l[2])

    @staticmethod
    def zeros():
        return Vector3(0, 0, 0)

    @staticmethod
    def ones():
        return Vector3(1, 1, 1)

    @staticmethod
    def forward():
        return Vector3(0, 0, 1)

    @staticmethod
    def backward():
        return Vector3(0, 0, -1)

    @staticmethod
    def up():
        return Vector3(0, 1, 0)

    @staticmethod
    def down():
        return Vector3(0, -1, 0)

    @staticmethod
    def right():
        return Vector3(1, 0, 0)

    @staticmethod
    def left():
        return Vector3(-1, 0, 0)
