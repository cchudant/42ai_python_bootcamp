from numbers import Number


class Vector():
    """A class representing a vector"""

    def __init__(self, v):
        if isinstance(v, int):
            self.v = [0.0] * v
            return

        if isinstance(v, tuple):
            self.v = [float(i) for i in range(*v)]
            return

        try:
            ite = iter(v)  # duck typing
            vf = list(v)

            if any(not isinstance(i, Number) for i in vf):
                raise TypeError('vector elements must be numbers')

            self.v = [float(i) for i in vf]

        except TypeError:
            raise TypeError('cannot create a vector with argument of type'
                            + type(v))

    def __str__(self):
        return '(Vector [{}])'.format(', '.join(str(i) for i in self.v))

    def __repr__(self):
        return 'Vector([{}])'.format(', '.join(str(i) for i in self.v))

    def __len__(self):
        return len(self.v)

    def __add__(self, other):
        if isinstance(other, Number):
            return Vector([i + other for i in self.v])
        if not isinstance(other, Vector):
            return NotImplemented
        if len(other) != len(self):
            raise ValueError('cannot add different-length vectors')
        return Vector([i + j for i, j in zip(self.v, other.v)])

    def __radd__(self, other):
        if isinstance(other, Number):
            return Vector([other + i for i in self.v])
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Number):
            return Vector([i - other for i in self.v])
        if not isinstance(other, Vector):
            return NotImplemented
        if len(other) != len(self):
            raise ValueError('cannot substract different-length vectors')
        return Vector([i - j for i, j in zip(self.v, other.v)])

    def __rsub__(self, other):
        if isinstance(other, Number):
            return Vector([other - i for i in self.v])
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Vector([i / other for i in self.v])
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, Number):
            return Vector([other / i for i in self.v])
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Number):
            return Vector([i * other for i in self.v])
        if not isinstance(other, Vector):
            return NotImplemented
        if len(other) != len(self):
            raise ValueError('cannot perform the dot product on' +
                             ' different-length vectors')
        return sum(i * j for i, j in zip(self.v, other.v))

    def __rmul__(self, other):
        if isinstance(other, Number):
            return Vector([other * i for i in self.v])
        return NotImplemented
