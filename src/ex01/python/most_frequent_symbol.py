def most_frequent_symbol(filename, print_symbol=False):
    """
    Returns and prints the most frequent symbol(character) in a file.
    
    :param filename: name of the file to search
    :param print_symbol: if true, prints the most frequent symbol

    :return the most frequent symbol
    """

    char_count = {}

    with open(filename) as file:
        for line in file:
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 0

    most_frequent = max(char_count, key=char_count.get)

    if print_symbol:
        print("Most frequent symbol: '{}'".format(most_frequent))

    return most_frequent


most_frequent_symbol("arithmetic_sequence.py")

"""
Most Frequent Symbol Tests

To run: pytest .\most_frequent_symbol.py
"""


def test_most_frequent_symbol_of_this_file():
    assert most_frequent_symbol(filename="most_frequent_symbol.py") == " "


def test_most_frequent_symbol_of_aux_file():
    assert most_frequent_symbol(filename="../../../docs/AuxFiles/Nomes.txt") == "\n"


def test_most_frequent_symbol_of_alice29_file():
    assert most_frequent_symbol(filename="../../../docs/CD_TestFiles/alice29.txt") == " "


def test_most_frequent_symbol_of_a_file():
    assert most_frequent_symbol(filename="../../../docs/CD_TestFiles/a.txt") == " "
