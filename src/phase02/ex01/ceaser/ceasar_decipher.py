from src.phase02.ex01.ceaser.ceasar_cipher import ASCII_PRINTABLE_CHARS_LENGTH
from src.utils.utils import entropy_from_list, show_histogram

ASCII_FIRST_PRINTABLE_CHAR = 32


def ceaser_decipher(input_file, output_file, s, show_hist=False):
    """
    Deciphers a ciphered text from an input file using Ceaser Cipher (https://en.wikipedia.org/wiki/Caesar_cipher).

    :param input_file: the input file to read the ciphered text from
    :param output_file: the output file to write the deciphered text to
    :param s: the shift value to use [must be an integer between 0 and 25]
    :param show_hist: when True, shows the histogram of the plain text and the cipher text
    """

    # Get ciphered text from file
    with open(input_file, 'r') as input_file:
        cipher_text = input_file.read()

    decipher_text = ""

    # Transverse the cipher text
    for i in range(len(cipher_text)):
        char = cipher_text[i]

        if char == '\n' or char == '\t' or char == '\r':
            decipher_text += char
            continue

        char_code = ord(char) - s
        if char_code < ASCII_FIRST_PRINTABLE_CHAR:
            char_code += ASCII_PRINTABLE_CHARS_LENGTH

        decipher_text += chr(char_code)

    # Write decipher text in output file
    with open(output_file, "w") as f:
        f.write(decipher_text)

    # Calculate and print entropy of the cipher text and the decipher text
    cipher_text_entropy = entropy_from_list(list(cipher_text))
    decipher_text_entropy = entropy_from_list(list(decipher_text))

    print("Cipher text entropy: ", cipher_text_entropy)
    print("Decipher text entropy: ", decipher_text_entropy)
    print()

    # Display histogram of the cipher text and the decipher text
    if show_hist:
        show_histogram(list(cipher_text), "Cipher text", "Cipher text Histogram (Ceaser)", cipher_text_entropy)
        show_histogram(list(decipher_text), "Decipher text", "Decipher text Histogram (Ceaser)", decipher_text_entropy)


# Decipher test files
if __name__ == '__main__':
    ceaser_decipher("ciphered_files/ceaser_cipher_text_alphabet.txt",
                    "deciphered_files/ceaser_decipher_text_alphabet.txt", 6, show_hist=True)

    ceaser_decipher("ciphered_files/ceaser_cipher_text_a.txt",
                    "deciphered_files/ceaser_decipher_text_a.txt", 4)

    ceaser_decipher("ciphered_files/ceaser_cipher_text_alice29.txt",
                    "deciphered_files/ceaser_decipher_text_alice29.txt", 10)
