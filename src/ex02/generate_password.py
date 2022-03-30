from strings_font import strings_font
import random

lowercase_letters_alphabet = list("abcdefghijklmnopqrstuvwxyz")
lowercase_letters_fmp = [1 / 26] * 26

uppercase_letters_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
uppercase_letters_fmp = [1 / 26] * 26

numbers_alphabet = list("0123456789")
numbers_fmp = [1 / 10] * 10

special_symbols_alphabet = list("~`! @#$%^&*()_-+={[}]|:;\"'<,>.?/")
special_symbols_fmp = [1 / 32] * 32

alphabets = [(lowercase_letters_alphabet, lowercase_letters_fmp),
             (uppercase_letters_alphabet, uppercase_letters_fmp),
             (numbers_alphabet, numbers_fmp),
             (special_symbols_alphabet, special_symbols_fmp)]

alphabets_size = len(alphabets)


def generate_password(min_length, max_length):
    """
    Generates a password with length in the range min_length and max_length.

    :param min_length: min password length
    :param max_length: max password length

    :return: generated password
    """

    if min_length < alphabets_size:
        print(f'Minimum password length should be at least {alphabets_size}.')
        return

    password_length = random.randint(min_length, max_length)
    print("Password length: ", password_length)

    password_length = password_length - alphabets_size

    counts = [1] * alphabets_size

    if password_length > 0:
        for i in range(password_length):
            counts_idx = random.randint(0, alphabets_size - 1)
            counts[counts_idx] += 1

    # Generate password
    password = ""
    for i, alphabet in enumerate(alphabets):
        password += strings_font(alphabet[0], alphabet[1], counts[i])

    # Shuffle password
    password = password.split(";")
    random.shuffle(password)
    password = "".join(password)

    print("Password: ", password)
    return password


if __name__ == '__main__':
    generate_password(100, 100)
