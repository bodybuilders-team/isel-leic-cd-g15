import re

MIN_PASSWORD_LENGTH = 8


def check_password_strength(password):
    """
    Verifies the password strength.

    :param password: password to test
    """

    weak_level = 0

    # Checking length
    if len(password) < MIN_PASSWORD_LENGTH:
        weak_level += 1
        print("Password must be at least 8 characters long")

    # Searching for digits
    if re.search(r"\d", password) is None:
        weak_level += 1
        print("Password should have digits")

    # Searching for uppercase letters
    if re.search(r"[A-Z]", password) is None:
        weak_level += 1
        print("Password should have uppercase letters")

    # Searching for lowercase letters
    if re.search(r"[a-z]", password) is None:
        weak_level += 1
        print("Password should have lowercase letters")

    # Searching for symbols
    if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None:
        weak_level += 1
        print("Password should have symbols")

    print()
    # Result
    match weak_level:
        case 0:
            print("Strong password")
        case 1 | 2 | 3:
            print("Moderate strength")
        case 4:
            print("Weak password")


# Test of check_password_strength
if __name__ == '__main__':
    check_password_strength("kt/3<^SigS>1A0'j")
