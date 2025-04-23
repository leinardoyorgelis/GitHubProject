def square_root(number):
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return number ** 0.5

try:
    result = square_root(-4)
except ValueError as e:
    print(e)
