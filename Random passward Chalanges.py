import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6."
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    # Ensure the password has at least one lowercase, one uppercase, and one digit
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    
    # Fill the rest of the password with random characters
    all_characters = lowercase + uppercase + digits
    password =password + random.choices(all_characters, k=length - len(password))
    
    # Shuffle to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
password_length = 10
password = generate_password(password_length)

print(f"Generated password: {password}")
