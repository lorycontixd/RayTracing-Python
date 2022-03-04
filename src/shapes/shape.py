from src.transform import Transform
from src.vector3 import Vector3
from src.quaternion import Quaternion
from src.ray import Ray

class Shape:
    def __init__(self, pos:Vector3=None, rot:Vector3=None, scale:Vector3=None):
        if not pos:
            position = Vector3.zeros()
        if not rot:
            rotation = Quaternion.Identity()
        if not scale:
            scale = Vector3.ones()
        self.transform = Transform(pos, rot, scale)

    def IntersectRay(self, r:Ray):
        pass


