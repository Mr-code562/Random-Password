import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    all_chars = string.ascii_letters + string.digits
    remaining = [random.choice(all_chars) for _ in range(length - 3)]
    password_list = [lower, upper, digit] + remaining
    random.shuffle(password_list)
    
    return ''.join(password_list)

print(generate_password(12))