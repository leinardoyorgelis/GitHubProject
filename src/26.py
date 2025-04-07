import random
from typing import List

def generate_random_string(length: int) -> str:
    """
    Generate a random string of specified length.
    
    Args:
    - length (int): The desired length of the generated string.

    Returns:
    - str: A randomly generated string of the given length.
    """
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

print(generate_random_string(10))  # Example usage: Generate a random string of length 10
