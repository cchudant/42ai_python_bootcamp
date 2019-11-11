import numpy as np

class ScrapBooker():
    def crop(array, dimensions, position):
        if dimensions > array.shape[:2]:
            raise ValueError('dimensions is larger than the image')
        return array[position[0]:, position[1]:][:dimensions[0], :dimensions[1]]

    def thin(array, n, axis):
        return np.delete(img, np.s_[::n], axis)

    def juxtapose(array, n, axis):
        return np.concatenate([array] * n, axis=axis)

    def mosaic(array, dimensions):
        return np.concatenate([np.concatenate([array] * dimensions[0], axis=0)] * dimensions[1], axis=1)
