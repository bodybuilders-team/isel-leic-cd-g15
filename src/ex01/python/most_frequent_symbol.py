def most_frequent_symbol(filename):
    """
    Prints the most frequent symbol(character) in a file.
    
    :param filename: name of the file to search
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

    print("Most frequent symbol: '{}'".format(most_frequent))


most_frequent_symbol("arithmetic_sequence.py")
