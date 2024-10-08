from src.utils.utils import entropy_from_list, show_histogram


def vernam_decipher(input_file, output_file, key, show_hist=False):
    """
    Deciphers a ciphered text from an input file using Vernam Cipher (https://en.wikipedia.org/wiki/One-time_pad).
    Only works with letters.

    :param input_file: the input file to read the ciphered text from
    :param output_file: the output file to write the deciphered text to
    :param key: the key to use for to decipher (preferably it should be the same length as the ciphered text)
    :param show_hist: when True, shows the histogram of the plain text and the cipher text
    """

    # Get ciphered text from file
    with open(input_file, 'rb') as input_file:
        cipher_text = input_file.read().decode()

    decipher_text = ""

    # Transverse the cipher text
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        key_char = key[i % len(key)]

        char_code = ord(char) ^ ord(key_char)
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
        show_histogram(list(cipher_text), "Cipher text", "Cipher text Histogram (Vernam)", cipher_text_entropy)
        show_histogram(list(decipher_text), "Decipher text", "Cipher text Histogram (Vernam)", decipher_text_entropy)


# Decipher test files
if __name__ == '__main__':
    vernam_decipher("ciphered_files/vernam_cipher_text_alphabet.txt",
                    "deciphered_files/vernam_decipher_text_alphabet.txt",
                    "abcdefghijklmnopqrstuvwxyz", show_hist=True)

    vernam_decipher("ciphered_files/vernam_cipher_text_a.txt",
                    "deciphered_files/vernam_decipher_text_a.txt",
                    "abcdefghijklmnopqrstuvwxyz")

    vernam_decipher("ciphered_files/vernam_cipher_text_alice29.txt",
                    "deciphered_files/vernam_decipher_text_alice29.txt",
                    "abcdefghijklmnopqrstuvwxyz")
