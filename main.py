import numpy as np

from src.vector3 import Vector3
from src.transform import Transform
from src.ray import Ray
from src.matrix import Matrix3


if __name__ == '__main__':
    v = Vector3(2,1,4)
    m = Matrix3([[1,1,1],[2,3,3],[1,2,3]])
    m2 = Matrix3([[3,3,3],[2,2,2],[1,1,1]])
    m3 = m.Mul(m2)
    m4 = m.Mul(v)
    print(v)
    m.Print()
    m4.Print()
