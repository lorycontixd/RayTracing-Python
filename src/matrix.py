import numpy as np
import pprint
from .vector3 import Vector3


class Matrix3:
    def __init__(self, array: np.array = None):
        array = np.array(array)
        if array is not None and array.shape == (3, 3):
            self.matrix = array
        else:
            self.matrix = np.identity(3)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix3(self.matrix * other)
        elif isinstance(other, Matrix3):
            return Matrix3(np.matmul(self.matrix, other.matrix))

    def __getitem__(self, item):
        return self.matrix[item]

    def Inverse(self):
        m = self.matrix
        det = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) \
              - m[0][1] * (m[1][0] * m[2][2] - m[2][0] * m[1][2]) \
              + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])

    def Transpose(self):
        m = Matrix3(np.array(
            [[self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]],
             [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1]],
             [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2]]]
        ))
        return m

    def Mul(self, other):
        if isinstance(other, (int, float)):
            return Matrix3(self.matrix * other)
        elif isinstance(other, Matrix3):
            return Matrix3(np.matmul(self.matrix, other.matrix))
        elif isinstance(other, Vector3):
            # return Matrix3(np.matmul(self.matrix, np.array([other.x, other.y, other.z])))
            l = []
            for row in self.matrix:
                val = other.x * row[0] + other.y * row[1] * other.z * row[2]
                if isinstance(val, (np.int32, np.int64)):
                    val = int(val)
                elif isinstance(val, (np.float32, np.float64)):
                    val = float(val)
                l.append(val)
            if len(l)==3:
                return Vector3.FromList(l)

    def Print(self):
        pprint.pprint(self.matrix)
