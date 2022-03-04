import numpy as np
from .matrix import Matrix3


class Transformation:
    def __init__(self):
        pass


class Translation(Transformation):
    def __init__(self, dx, dy, dz):
        self.matrix = Matrix3([
            [1,0,]
        ])