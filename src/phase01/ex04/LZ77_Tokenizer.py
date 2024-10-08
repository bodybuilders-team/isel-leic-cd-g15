from src.utils.utils import entropy_from_list, show_histogram

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


# Encode test files
if __name__ == '__main__':
    LZ77_Tokenizer("../../../docs/CD_TestFiles/a.txt", "encoded_test_files/a_encoded.txt", sw_length=20, lab_length=8,
                   show_hist=True)
    LZ77_Tokenizer("../../../docs/CD_TestFiles/alice29.txt", "encoded_test_files/alice29_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../../docs/CD_TestFiles/cp.htm", "encoded_test_files/cp_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../../docs/CD_TestFiles/Person.java", "encoded_test_files/Person_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../../docs/CD_TestFiles/progc.c", "encoded_test_files/progc_encoded.txt", 8, 4)
