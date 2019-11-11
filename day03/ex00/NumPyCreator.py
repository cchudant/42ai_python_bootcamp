import numpy as np

def from_list(lst, dtype=None):
    return np.array(lst, dtype=dtype)

def from_tuple(tup, dtype=None):
    return np.array(tup, dtype=dtype)

def from_iterable(ite, dtype=None):
    return np.array(ite, dtype=dtype)

def from_shape(shape, val, dtype=None):
    return np.full(shape, val, dtype=dtype)

def random(shape, dtype=None):
    return np.random.random(shape, dtype=dtype)

def identity(n, dtype=None):
    return np.eye(n, dtype=dtype)
