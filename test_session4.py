import pytest
import random
import session4
import os
import math


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_incorrect_inputnum():
    with pytest.raises(ValueError):
        r = session4.Qualean(2)
    with pytest.raises(ValueError):
        r = session4.Qualean(-2)
    with pytest.raises(ValueError):
        r = session4.Qualean(-1.34)


def test_inputnum_zero():
    assert session4.Qualean(0), "There seems to be something basic going wrong! Not even able to create a class"


def test_inputnum():
    r = random.randint(-1, 1)
    assert session4.Qualean(r), "There seems to be something basic going wrong! Not even able to create a class"


def test_add():
    r = session4.Qualean(random.randint(-1, 1))
    q = session4.Qualean(0)
    for _ in range(100):
        q = q + r
    assert math.isclose(q, 100 * r, rel_tol=0.02), "100*q is not close to q added 100 times"


def test_or():
    assert session4.Qualean(0) or session4.Qualean(1)


def test_and():
    assert session4.Qualean(0) and session4.Qualean(1)
