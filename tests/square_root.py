import cmath  # Importing cmath for complex number operations

class Roots:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

def calculate_delta(a: float, b: float, c: float) -> float:
    return b**2 - 4*a*c

def square_root(a: float, b: float, c: float):
    delta = calculate_delta(a, b, c)
    if delta > 0:
        root1 = (-b + cmath.sqrt(delta)) / (2 * a)
        root2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return Roots(root1, root2, delta)
    elif delta == 0:
        root = -b / (2 * a)
        return Roots(root, root, delta)
    else:  # delta < 0
        root1 = (-b + cmath.sqrt(delta)) / (2 * a)
        root2 = (-b - cmath.sqrt(delta)) / (2 * a)
        return Roots(root1, root2, delta)


def test_calculate_delta():
    assert calculate_delta(1, 0, -1) == 4
    assert calculate_delta(1, -2, 1) == 0
    assert calculate_delta(1, 0, 1) == -4

def test_square_root():
    roots = square_root(1, 0, -1)
    assert roots.a == 1
    assert roots.b == -1
    assert roots.c == 4

    roots = square_root(1, -2, 1)
    assert roots.a == 1
    assert roots.b == 1
    assert roots.c == 0

    roots = square_root(1, 0, 1)
    assert roots.a == cmath.sqrt(-1)
    assert roots.b == -cmath.sqrt(-1)
    assert roots.c == -4
