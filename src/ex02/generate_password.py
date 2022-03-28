from strings_font import strings_font
import random


lowercase_letters_alphabet = list("abcdefghijklmnopqrstuvwxyz")
lowercase_letters_fmp = [1/26 for i in range(26)]

uppercase_letters_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
uppercase_letters_fmp = [1/26 for i in range(26)]

numbers_alphabet = list("0123456789")
numbers_fmp = [1/10 for i in range(10)]

special_symbols_alphabet = list("~`! @#$%^&*()_-+={[}]|:;\"'<,>.?/")
special_symbols_fmp = [1/32 for i in range(32)]

alphabets = [(lowercase_letters_alphabet, lowercase_letters_fmp),
             (uppercase_letters_alphabet, uppercase_letters_fmp),
             (numbers_alphabet, numbers_fmp),
             (special_symbols_alphabet, special_symbols_fmp)]

alphabets_size = len(alphabets)


def generate_password(min_length, max_length):
    """
    Generates a password with length in the range min_length and max_length.

    :return:
    """
    if min_length < alphabets_size:
        print(f'Minimum password length should be at least {alphabets_size}.')
        return

    password_length = random.randint(min_length, max_length)

    print(password_length)

    password_length = password_length - alphabets_size

    counts = [1 for i in range(alphabets_size)]

    if password_length > 0:
        for i in range(password_length):
            counts_idx = random.randint(0, alphabets_size - 1)
            counts[counts_idx] += 1

    password = ""
    for i, alphabet in enumerate(alphabets):
        password += strings_font(alphabet[0], alphabet[1], counts[i], False, False)

    password = password.split(";")
    random.shuffle(password)

    print("".join(password))


if __name__ == '__main__':
    generate_password(100, 100)
