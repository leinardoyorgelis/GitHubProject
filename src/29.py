import random

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

if __name__ == "__main__":
    # Generate a random list with even numbers between 1 and 10 (inclusive)
    even_numbers = [random.randint(1, 10) for _ in range(random.randint(5, 8))]
    
    print("Even numbers:", even_numbers)
    print("Shuffled list of even numbers:", shuffle_list(even_numbers))
