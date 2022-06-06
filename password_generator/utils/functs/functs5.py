import secrets
import string
import uuid


def generate_uuid():
    password = uuid.uuid4()
    return password


# 5 char functions
def five_generate_only_letter():
    password_characters = string.ascii_letters
    password = ''.join(secrets.choice(password_characters) for _ in range(5))
    return password


def five_generate_letters_nums_symbols():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for _ in range(5))
    return password


def five_generate_letters_nums():
    password_characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(password_characters) for _ in range(5))
    return password


def five_generate_hexadecimal():
    password = secrets.token_hex(5)
    return password
