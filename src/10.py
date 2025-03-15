import random

def generate_random_string(length=10):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for i in range(length))

print(generate_random_string())
