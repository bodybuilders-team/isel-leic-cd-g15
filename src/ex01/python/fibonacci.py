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


print_fibonacci(20)
