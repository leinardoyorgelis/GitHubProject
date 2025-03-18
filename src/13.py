import random

def get_random_python_code():
    # Generate a random number between 1 and 10
    rand_num = random.randint(1, 10)

    if rand_num % 2 == 0:
        return "print('Hello World!')"
    else:
        return "my_list = [1, 2, 3, 4, 5]"