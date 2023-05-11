import random
import string

def generate_password(length):
    """Generate a random password of the specified length"""
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == '__main__':
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated password:", password)

