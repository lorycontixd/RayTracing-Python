import sys
from .vector3 import Vector3


class Ray:
    def __init__(self, origin: Vector3 = None, direction: Vector3 = None, tmax: float = None):
        self.origin = origin
        self.direction = direction
        self.tmax = tmax
        if self.origin is None:
            self.origin = Vector3.ones()
        if self.direction is None:
            self.direction = Vector3.forward()
        if self.tmax is None:
            self.tmax = sys.float_info.max

        self.time = 0

    def __getattr__(self, item):
        assert isinstance(item, (int, float))
        return self.GetPoint(item)

    def GetPoint(self, t: float):
        if t <= self.tmax:
            return self.origin + self.direction * t
        else:
            return self.origin + self.direction * self.tmax
