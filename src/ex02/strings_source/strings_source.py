import random
import matplotlib.pyplot as plt
from scipy.stats import entropy


def strings_source(alphabet, fmp, L, file="strings_source.txt", write_file=False, show_hist=False):
    """
    Generates a sequence of L strings, separated by ";".
    Prints the entropy.

    :param alphabet: list of possible strings
    :param fmp: function of mass probability for the alphabet
    :param L: number of strings to generate
    :param file: file to write the sequence
    :param write_file: when True, writes the sequence in a file
    :param show_hist: when True, shows the sequence histogram

    :return: sequence of strings

    Example: strings_source(["abc", "cde"], [0.7, 0.3], 3) -> "abc;abc;cde"
    """

    # Calculate and print entropy
    e = round(entropy(fmp, base=2), ndigits=4)
    print("Entropy: ", e)

    # Get string sequence
    strs = random.choices(alphabet, fmp, k=L)
    res = ";".join(strs)
    print("Sequence: ", res)

    # Write sequence in file
    if write_file:
        with open(file, "w") as f:
            f.write(res)

    # Display sequence histogram
    if show_hist:
        plt.hist(strs, bins=len(strs))
        plt.xlabel("Alphabet")
        plt.ylabel("Occurrences")
        plt.suptitle("Strings Source Histogram", fontsize=18)
        plt.title("Entropy: " + str(e))
        plt.show()

    return res


#  Test of strings_source
if __name__ == '__main__':
    a = ["abc", "hbo", "xpto", "brba", "cbo", "foo", "bar"]
    a_fmp = [3 / 16, 1 / 16, 6 / 16, 2 / 16, 1 / 16, 2 / 16, 1 / 16]

    strings_source(a, a_fmp, 100, write_file=True, show_hist=True)
