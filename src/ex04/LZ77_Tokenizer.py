def LZ77_Tokenizer(input_file, output_file, sw_length, lab_length):
    """
    Creates a text file with the tokens obtained from the processing of the received file.
    Presents the histogram and entropy of the fields "position" and "length" of the tokens.

    :param input_file: file to tokenize
    :param output_file: file where the tokens will be printed
    :param sw_length: search window length
    :param lab_length: look-ahead-buffer length
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
        return (-1, -1, "")

    if sw_len == 0:
        return (0, 0, lab[0])

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

    return (best_position, best_length, innovation_symbol)

# TODO Apresenta os histogramas e a entropia dos campos position e length
# TODO Comente os resultados obtidos

# Encode test files
if __name__ == '__main__':
    LZ77_Tokenizer("../../docs/CD_TestFiles/a.txt", "a_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../docs/CD_TestFiles/alice29.txt", "alice29_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../docs/CD_TestFiles/cp.htm", "cp_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../docs/CD_TestFiles/Person.java", "Person_encoded.txt", 8, 4)
    LZ77_Tokenizer("../../docs/CD_TestFiles/progc.c", "progc_encoded.txt", 8, 4)
