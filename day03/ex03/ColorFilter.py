import numpy as np


class ColorFilter():
    def invert(array):
        return 1 - array

    def to_blue(array):
        array[:, :, 2] =* 1.2
        return array

    def to_green(array):
        array[:, :, 1] *= 1.2
        return array

    def to_red(array):
        array[:, :, 0] *= 1.2
        return array
