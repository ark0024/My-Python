import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

length = int(input("Kitne characters ka password chahiye? "))
password = generate_password(length)
print("Genetated Password:", password)

