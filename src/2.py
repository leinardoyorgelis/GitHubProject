import random
def generate_random_python_code():
    """
    Generates a random Python code snippet
    """
    # List of all the possible Python statements
    statements = ["x = 5", "y = 'hello'", "z = True", "print(x, y, z)"]
    
    # Pick a random statement from the list
    statement = random.choice(statements)
    
    # Return the generated code
    return statement