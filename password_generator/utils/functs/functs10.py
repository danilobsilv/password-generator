import secrets
import string


def ten_generate_only_letter():
    password_characters = string.ascii_letters
    password = ''.join(secrets.choice(password_characters) for _ in range(10))
    return password


def ten_generate_letters_nums():
    password_characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(password_characters) for _ in range(10))
    return password


def ten_generate_letters_nums_symbols():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for _ in range(10))
    return password


def ten_generate_hexadecimal():
    password = secrets.token_hex(10)
    return password
