import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    character_set = ''
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special_chars:
        character_set += string.punctuation

    if not character_set:
        return "Error: No character set selected"

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password