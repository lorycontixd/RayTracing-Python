import numpy as np

from .matrix import Matrix3
from .vector3 import Vector3


class Transform:
    def __init__(self, position=None, rotation=None, scale=None):
        self.position = position
        self.rotation = rotation
        self.scale = scale

        if self.position is None:
            self.position = Vector3.zeros()
        if self.scale is None:
            self.scale = Vector3.ones()

    def GetPosition(self):
        return self.position

    def GetScale(self):
        return self.scale

    def GetRotation(self):
        return self.rotation

    def Translate(self, translation:Vector3):
        self.position = self.position + translation

    def Rotate(self, rotation:Matrix3):
        self.rotation

    @staticmethod
    def forward():
        return Vector3(0, 0, 1)

    @staticmethod
    def up():
        return Vector3(0, 1, 0)

    @staticmethod
    def right():
        return Vector3(1, 1, 0)


