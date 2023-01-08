import pytest
from rdp_testcase.testcase3.lisp import one, two, three, plus, minus, div, Digit


def test_example_1():
    assert str(one(div(two()))) == str(0.5)


def test_example_2():
    assert str(one(plus(three()))) == str(4)


def test_example_3():
    assert str(one(plus(three(minus(two()))))) == str(2)
