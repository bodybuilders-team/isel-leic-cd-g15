from src.utils.utils import entropy_from_list, show_histogram

ALPHABET_LENGTH = 26
UPPERCASE_OFFSET = 65
LOWERCASE_OFFSET = 97


def ceaser_decipher(input_file, output_file, s, show_hist=False):
    """
    Deciphers a ciphered text from an input file using Ceaser Cipher (https://en.wikipedia.org/wiki/Caesar_cipher).
    Only works with letters.

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

        # Decrypt uppercase characters in cipher text
        if char.isupper():
            decipher_text += chr(
                (ord(char) + (ALPHABET_LENGTH - s) - UPPERCASE_OFFSET) % ALPHABET_LENGTH + UPPERCASE_OFFSET)
        # Decrypt lowercase characters in cipher text
        else:
            decipher_text += chr(
                (ord(char) + (ALPHABET_LENGTH - s) - LOWERCASE_OFFSET) % ALPHABET_LENGTH + LOWERCASE_OFFSET)

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
        show_histogram(list(decipher_text), "Decipher text", "Cipher text Histogram (Ceaser)", decipher_text_entropy)


# Decipher test files
if __name__ == '__main__':
    ceaser_decipher("ciphered_files/ceaser_cipher_text_alphabet.txt",
                    "deciphered_files/ceaser_decipher_text_alphabet.txt", 6, show_hist=True)
    ceaser_decipher("ciphered_files/ceaser_cipher_text_a.txt",
                    "deciphered_files/ceaser_decipher_text_a.txt", 4)
    ceaser_decipher("ciphered_files/ceaser_cipher_text_alice29.txt",
                    "deciphered_files/ceaser_decipher_text_alice29.txt", 10)
