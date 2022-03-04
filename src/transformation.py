import numpy
import numpy as np


class Transformation:
    def __init__(self, matrix:np.ndarray=None):
        if not matrix:
            matrix = np.identity(4)
