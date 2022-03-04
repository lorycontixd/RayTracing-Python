import numpy as np

from src.vector3 import Vector3
from src.transform import Transform
from src.ray import Ray
from src.matrix import Matrix3


if __name__ == '__main__':
    v = Vector3(1,1,1)
    m = Matrix3([[1,2,3],[10,1,1],[2,3,1]])
    m.Identity().Transpose().Print()

