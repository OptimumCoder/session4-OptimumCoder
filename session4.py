import math
import random
import cmath

class Qualean:
    """
    This class is going to do wonders shortly
    """
    def __init__(self, inputnum):
        self.inputnum = inputnum

    @property
    def inputnum(self):
        return self._inputnum

    @inputnum.setter
    def inputnum(self, inputnum):
        if inputnum not in [-1, 0, 1]:
            raise ValueError("Incorrect input")
        else:
            self._inputnum = inputnum

    def roundednum(self, a):
        a = self._inputnum * random.uniform(-1, 1)
        return round(a, 10)

    def __and__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum and other._inputnum
        else:
            raise NotImplementedError("not implemented and")

    def __or__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum or other._inputnum
        else:
            raise NotImplementedError("not implemented or")

    def __str__(self):
        return "Qualean: inputnum {0}".format(self._inputnum)

    def __repr__(self):
        return "Qualean({0})".format(self._inputnum)

    def __add__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum + other._inputnum
        else:
            raise NotImplementedError("not implemented add")

    def __eq__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum == other._inputnum
        else:
            raise NotImplementedError("not implemented equal")

    def __float__(self):
        return float(self._inputnum)

    def __ge__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum > other._inputnum or self._inputnum == other._inputnum
        else:
            raise NotImplementedError("not implemented greater than or equal to")

    def __gt__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum > other._inputnum
        else:
            raise NotImplementedError("not implemented greater than")

    def __invertsign__(self):
        return -1 * self._inputnum

    def __le__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum < other._inputnum or self._inputnum == other._inputnum
        else:
            raise NotImplementedError("not implemented lesser than or equal to")

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum < other._inputnum
        else:
            raise NotImplementedError("not implemented lesser than")

    def __mul__(self, other):
        if isinstance(other, Qualean):
            return self._inputnum * other._inputnum
        else:
            raise NotImplementedError("not implemented multiply")

    def __sqrt__(self):
        if self._inputnum < 0:
            return cmath.sqrt(self._inputnum)
        else:
            return math.sqrt(self._inputnum)

    def __bool__(self):
        return bool(self._inputnum)

