import numpy as np
from scipy.stats import entropy
import matplotlib.pyplot as plt

TOKEN_POSITION_IDX = 0
TOKEN_LENGTH_IDX = 1


def LZ77_Tokenizer(input_file, output_file, sw_length, lab_length, show_hist=False):
    """
    Creates a text file with the tokens obtained from the processing of the received file.
    Presents the histogram and entropy of the fields "position" and "length" of the tokens.

    :param input_file: file to tokenize
    :param output_file: file where the tokens will be printed
    :param sw_length: search window length
    :param lab_length: look-ahead-buffer length
    :param show_hist: when True, shows the histogram of the fields "position" and "length" of the tokens
    """

    i = 0
    sw_i = 0
    tokens = []

    # Get data from file
    with open(input_file, 'r') as input_file:
        data = input_file.read()

    # Get tokens
    while i < len(data):
        sw = data[sw_i:i]
        lab = data[i:i + lab_length]

        token = LZ77_get_token(sw, lab)
        tokens.append(token)

        i += token[1] + 1
        sw_i = i - sw_length

        if sw_i < 0:
            sw_i = 0

    # Write tokens in output file
    with open(output_file, "w") as f:
        for token in tokens:
            f.write(str(token) + '\n')

    # Calculate and print entropy of the fields "position" and "length"
    positions = list(map(lambda t: t[TOKEN_POSITION_IDX], tokens))
    lengths = list(map(lambda t: t[TOKEN_LENGTH_IDX], tokens))

    positions_entropy = entropy_from_list(positions)
    lengths_entropy = entropy_from_list(lengths)

    print("'Position' field entropy: ", positions_entropy)
    print("'Length' field entropy: ", lengths_entropy)
    print()

    # Display histogram of the fields "position" and "length"
    if show_hist:
        show_histogram(positions, "Tokens 'position'", "Tokens 'position' field Histogram", positions_entropy)
        show_histogram(lengths, "Tokens 'length'", "Tokens 'length' field Histogram", lengths_entropy)


def show_histogram(labels, x_label, title, labels_entropy):
    """
    Shows a histogram of labels.
    :param labels: histogram labels
    :param x_label: histogram x label
    :param title: histogram title
    :param labels_entropy: labels entropy
    """

    plt.hist(labels, bins=len(labels))
    plt.xlabel(x_label)
    plt.ylabel("Occurrences")
    plt.suptitle(title, fontsize=18)
    plt.title("Entropy: " + str(labels_entropy))
    plt.show()


def LZ77_get_token(sw, lab):
    """
    Gets the token for the look-ahead-buffer in the search window.

    :param sw: search window
    :param lab: look-ahead buffer
    :return: token
    """

    sw_len = len(sw)
    lab_len = len(lab)

    if lab_len == 0:
        return -1, -1, ""

    if sw_len == 0:
        return 0, 0, lab[0]

    best_length = 0
    best_position = 0

    for i in range(sw_len):
        length = 0
        while i + length < sw_len and length < lab_len and sw[i + length] == lab[length]:
            length += 1

        if length > best_length:
            best_position = i
            best_length = length

    innovation_symbol = lab[best_length - 1] if best_length == lab_len else lab[best_length]

    return best_position, best_length, innovation_symbol


def entropy_from_list(labels):
    """
    Calculates entropy from a list.
    :param labels: list
    :return: entropy
    """

    value, counts = np.unique(labels, return_counts=True)
    return round(entropy(counts, base=2), ndigits=4)


# TODO Comente os resultados obtidos

# Encode test files
if __name__ == '__main__':
    LZ77_Tokenizer("../../docs/CD_TestFiles/a.txt", "a_encoded.txt", sw_length=8, lab_length=4, show_hist=True)
    LZ77_Tokenizer("../../docs/CD_TestFiles/alice29.txt", "alice29_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../docs/CD_TestFiles/cp.htm", "cp_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../docs/CD_TestFiles/Person.java", "Person_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../docs/CD_TestFiles/progc.c", "progc_encoded.txt", 8, 4)
