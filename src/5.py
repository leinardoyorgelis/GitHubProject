import random

def generate_random_python_code(length):
    code = []
    for i in range(length):
        line = ""
        for j in range(5):
            line += chr(random.randint(97, 122))
        code.append(line)
    return "\n".join(code)