from src.utils.utils import entropy_from_list, show_histogram

ALPHABET_LENGTH = 26
UPPERCASE_OFFSET = 65
LOWERCASE_OFFSET = 97


def ceaser_cipher(input_file, output_file, s, show_hist=False):
    """
    Ciphers a plain text from an input file using Ceaser Cipher (https://en.wikipedia.org/wiki/Caesar_cipher).
    Only works with letters.

    :param input_file: the input file to read the plain text from
    :param output_file: the output file to write the ciphered text to
    :param s: the shift value to use [must be an integer between 0 and 25]
    :param show_hist: when True, shows the histogram of the plain text and the cipher text
    """

    # Get plain text from file
    with open(input_file, 'r') as input_file:
        plain_text = input_file.read()

    cipher_text = ""

    # Transverse the plain text
    for i in range(len(plain_text)):
        char = plain_text[i]

        # Encrypt uppercase characters in plain text
        if char.isupper():
            cipher_text += chr((ord(char) + s - UPPERCASE_OFFSET) % ALPHABET_LENGTH + UPPERCASE_OFFSET)
        # Encrypt lowercase characters in plain text
        else:
            cipher_text += chr((ord(char) + s - LOWERCASE_OFFSET) % ALPHABET_LENGTH + LOWERCASE_OFFSET)

    # Write cipher text in output file
    with open(output_file, "w") as f:
        f.write(cipher_text)

    # Calculate and print entropy of the plain text and the cipher text
    plain_text_entropy = entropy_from_list(list(plain_text))
    cipher_text_entropy = entropy_from_list(list(cipher_text))

    print("Plain text entropy: ", plain_text_entropy)
    print("Cipher text entropy: ", cipher_text_entropy)
    print()

    # Display histogram of the plain text and the cipher text
    if show_hist:
        show_histogram(list(plain_text), "Plain text", "Plain text Histogram (Ceaser)", plain_text_entropy)
        show_histogram(list(cipher_text), "Cipher text", "Cipher text Histogram (Ceaser)", cipher_text_entropy)


# Cipher test files
if __name__ == '__main__':
    ceaser_cipher("../../../../docs/CD_TestFiles/alphabet.txt", "ciphered_files/ceaser_cipher_text_alphabet.txt", 6,
                  show_hist=True)
    ceaser_cipher("../../../../docs/CD_TestFiles/a.txt", "ciphered_files/ceaser_cipher_text_a.txt", 4)
    ceaser_cipher("../../../../docs/CD_TestFiles/alice29.txt", "ciphered_files/ceaser_cipher_text_alice29.txt", 10)
