from functools import reduce

def fibonacci_sequence(n: int):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        return reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

def test_fibonacci_sequence():
    assert fibonacci_sequence(1) == [0]
    assert fibonacci_sequence(2) == [0, 1]
    assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_sequence(0) == []