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


print_arithmetic_sequence(50, 5, 5)
