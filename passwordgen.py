import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

try:
    password_length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

password = generate_password(password_length)
print(f"Generated Password: {password}")

