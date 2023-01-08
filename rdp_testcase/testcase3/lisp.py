from typing import Optional


class Digit:
    def __init__(self, val: int, acc: Optional[str] = None):
        self.val = val
        self.acc = acc

    def set_val(self, val):
        self.val = val

    def set_acc(self, acc):
        print(f"acc is set {acc}")
        self.acc = acc

    def eval(self, a: int):
        print(f"{a}{self.acc}{self.val}")
        self.val = eval(f"{a}{self.acc}{self.val}")
        self.acc = None

    def __str__(self) -> str:
        return str(self.val)


def one(a: Optional[Digit] = None) -> Digit:
    if type(a) is Digit:
        a.eval(1)
        return a
    else:
        return Digit(1)


def two(a: Optional[Digit] = None) -> Digit:
    if type(a) is Digit:
        a.eval(2)
        return a
    else:
        return Digit(2)


def three(a: Optional[Digit] = None) -> Digit:
    if type(a) is Digit:
        a.eval(3)
        return a
    else:
        return Digit(3)


def four(a: Optional[Digit] = None) -> Digit:
    if type(a) is Digit:
        a.eval(4)
        return a
    else:
        return Digit(4)


def five(a: Optional[Digit] = None) -> Digit:
    if type(a) is Digit:
        a.eval(5)
        return a
    else:
        return Digit(5)


def plus(a: Digit) -> Digit:
    a.set_acc("+")
    return a


def minus(a: Digit) -> Digit:
    a.set_acc("-")
    return a


def mult(a: Digit) -> Digit:
    a.set_acc("*")
    return a


def div(a: Digit) -> Digit:
    a.set_acc("/")
    return a
