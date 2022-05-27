from src.utils.utils import entropy_from_list, show_histogram

ASCII_PRINTABLE_CHARS_LENGTH = 95
ASCII_LAST_PRINTABLE_CHAR = 126


def vernam_cipher(input_file, output_file, key, show_hist=False):
    """
    Ciphers a plain text from an input file using Vernam Cipher (https://en.wikipedia.org/wiki/One-time_pad).
    Only works with letters.

    :param input_file: the input file to read the plain text from
    :param output_file: the output file to write the ciphered text to
    :param key: the key to use for the cipher (preferably it should be the same length as the plain text)
    :param show_hist: when True, shows the histogram of the plain text and the cipher text
    """

    # Get plain text from file
    with open(input_file, 'r') as input_file:
        plain_text = input_file.read()

    cipher_text = ""

    # Transverse the plain text
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i % len(key)]

        char_code = ord(char) ^ ord(key_char)
        cipher_text += chr(char_code)

    # Write cipher text in output file
    with open(output_file, "wb") as f:
        f.write(str.encode(cipher_text))

    # Calculate and print entropy of the plain text and the cipher text
    plain_text_entropy = entropy_from_list(list(plain_text))
    cipher_text_entropy = entropy_from_list(list(cipher_text))

    print("Plain text entropy: ", plain_text_entropy)
    print("Cipher text entropy: ", cipher_text_entropy)
    print()

    # Display histogram of the plain text and the cipher text
    if show_hist:
        show_histogram(list(plain_text), "Plain text", "Plain text Histogram (Vernam)", plain_text_entropy)
        show_histogram(list(cipher_text), "Cipher text", "Cipher text Histogram (Vernam)", cipher_text_entropy)


# Cipher test files
if __name__ == '__main__':
    vernam_cipher("../../../../docs/CD_TestFiles/alphabet.txt",
                  "ciphered_files/vernam_cipher_text_alphabet.txt",
                  "abcdefghijklmnopqrstuvwxyz", show_hist=True)

    vernam_cipher("../../../../docs/CD_TestFiles/a.txt",
                  "ciphered_files/vernam_cipher_text_a.txt",
                  "abcdefghijklmnopqrstuvwxyz")

    vernam_cipher("../../../../docs/CD_TestFiles/alice29.txt",
                  "ciphered_files/vernam_cipher_text_alice29.txt",
                  "abcdefghijklmnopqrstuvwxyz")
