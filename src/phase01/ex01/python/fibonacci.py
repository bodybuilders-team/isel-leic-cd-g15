def fibonacci(n):
    """
    Calculates the nth element of Fibonacci sequence.
    More about Fibonacci Sequence: https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci
    
    :param n: position of the element to return
    
    :return: nth element of Fibonacci sequence
    """

    if n in range(3):
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci(n):
    """
    Prints the first n elements of the Fibonacci sequence
    
    :param n: number of terms to be printed
    """

    for i in range(n):
        print(fibonacci(i))


"""
Fibonacci Tests

To run: pytest .\fibonacci.py
"""


def test_fibonacci_of_zero():
    assert fibonacci(0) == 1


def test_fibonacci_of_one():
    assert fibonacci(1) == 1


def test_fibonacci_of_two():
    assert fibonacci(2) == 1


def test_fibonacci_of_ten():
    assert fibonacci(10) == 55


def test_fibonacci_of_one_hundred():
    assert fibonacci(30) == 832040
