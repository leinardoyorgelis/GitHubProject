import random
def get_random_code(length=16):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join((random.choice(letters) for i in range(length)))