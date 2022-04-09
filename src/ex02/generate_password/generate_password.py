from src.ex02.strings_source.strings_source import strings_source
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

PASSWORD_MIN_LEN_DEFAULT = 8
PASSWORD_MAX_LEN_DEFAULT = 16


def generate_password(min_length=PASSWORD_MIN_LEN_DEFAULT, max_length=PASSWORD_MAX_LEN_DEFAULT):
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
        password += strings_source(alphabet[0], alphabet[1], counts[i])

    # Shuffle password
    password = password.split(";")
    random.shuffle(password)
    password = "".join(password)

    print("\nPassword: ", password)
    return password


FILES = 5
PASSWORDS_PER_FILE = 1000

# Write passwords in files
if __name__ == '__main__':
    for i in range(FILES):
        with open(f"passwords{i}.txt", "w") as f:
            for j in range(PASSWORDS_PER_FILE):
                f.write(generate_password() + "\n")
