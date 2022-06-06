import secrets
import string


def eight_generate_only_letter():
    password_characters = string.ascii_letters
    password = ''.join(secrets.choice(password_characters) for _ in range(8))
    return password


def eight_generate_letters_nums():
    password_characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(password_characters) for _ in range(8))
    return password


def eight_generate_letters_nums_symbols():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for _ in range(8))
    return password


def eight_generate_hexadecimal():
    password = secrets.token_hex(8)
    return password
