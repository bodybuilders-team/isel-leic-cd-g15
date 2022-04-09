def arithmetic_sequence(n, u, r):
    """
    Calculates the nth term of an arithmetic sequence.
    More about arithmetic sequences: https://en.wikipedia.org/wiki/Arithmetic_progression
    
    :param n: the nth term to be calculated
    :param u: value of first term
    :param r: difference between consecutive terms
    
    :return: the nth term of the arithmetic sequence
    """

    return u + (n - 1) * r


def print_arithmetic_sequence(n, u, r):
    """
    Prints the n first terms of an arithmetic sequence.
    
    :param n: number of terms to be printed
    :param u: value of first term
    :param r: difference between consecutive terms
    """

    for i in range(n):
        print(arithmetic_sequence(i, u, r))


"""
Arithmetic Sequence Tests

To run: pytest .\arithmetic_sequence.py
"""


def test_arithmetic_sequence_with_zero_r():
    assert arithmetic_sequence(n=10, u=1, r=0) == 1


def test_arithmetic_sequence_with_positive_r():
    assert arithmetic_sequence(n=10, u=1, r=5) == 46


def test_arithmetic_sequence_with_negative_r():
    assert arithmetic_sequence(n=10, u=1, r=-5) == -44


def test_arithmetic_sequence_of_zero():
    assert arithmetic_sequence(n=0, u=0, r=0) == 0


def test_arithmetic_sequence_of_one_hundred():
    assert arithmetic_sequence(n=100, u=1, r=1) == 100
