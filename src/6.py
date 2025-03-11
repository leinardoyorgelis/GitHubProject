def get_random_python_code():
    import random
    code = "".join(chr(ord('a') + (random.randint(0, 25))) for i in range(10))
    return code
