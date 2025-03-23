import random

def generate_code():
    # Generate some random numbers and characters
    numbers = list(range(10))
    words = ["Python", "School", "GitHub"]
    
    # Shuffle the generated words
    shuffled_words = random.sample(words, len(words))
    
    # Select a random word to form the code
    code = ''.join(shuffled_words)
    
    return code

# Generate and print the code
print(generate_code())
