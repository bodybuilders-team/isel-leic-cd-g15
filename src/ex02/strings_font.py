import random
import math
import matplotlib.pyplot as plt


def strings_font(alphabet, fmp, n, write_file, show_hist):
    """
    Generates a sequence of L strings, separated by ";".
    Prints the entropy.

    :param alphabet: list of possible strings
    :param fmp: function of mass probability for the alphabet
    :param n: number of strings to generate
    :param write_file: when True, writes the sequence in a file
    :param show_hist: when True, shows the sequence histogram

    :return: sequence of strings

    Example: strings_font(["abc", "cde"], [0.7, 0.3], 3) -> "abc;abc;cde"
    """

    # Calculate and print entropy
    entropy = calculate_entropy(fmp)
    print("Entropy: ", entropy)

    # Get string sequence
    strs = random.choices(alphabet, fmp, k=n)
    res = ";".join(strs)
    print("Sequence: ", res)

    # Write sequence in file
    if write_file:
        with open("strings_font", "w") as f:
            f.write(res)

    # Display sequence histogram
    if show_hist:
        plt.hist(strs, bins=len(strs))
        plt.xlabel("Alphabet")
        plt.ylabel("Occurrences")
        plt.suptitle("Strings Font Histogram", fontsize=18)
        plt.title("Entropy: " + str(calculate_entropy(fmp)))
        plt.show()

    return res


def calculate_entropy(fmp):
    """
    Calculates the entropy of a function of mass probability.

    :param fmp: function of mass probability

    :return: entropy
    """

    return sum(map(lambda prob: prob * math.log(prob, 2), fmp)) * -1


if __name__ == '__main__':
    #  Test of strings_font
    a = ["abc", "hbo", "xpto", "brba", "cbo", "foo", "bar"]
    a_fmp = [3 / 16, 1 / 16, 6 / 16, 2 / 16, 1 / 16, 2 / 16, 1 / 16]

    strings_font(a, a_fmp, 100, write_file=True, show_hist=True)
