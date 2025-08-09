import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Ensure at least one character from each category
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    
    # Fill the rest of the password length with random choices
    all_chars = string.ascii_letters + string.digits
    remaining = [random.choice(all_chars) for _ in range(length - 3)]
    
    # Combine and shuffle
    password_list = [lower, upper, digit] + remaining
    random.shuffle(password_list)
    
    return ''.join(password_list)

# Example usage
print(generate_password(12))