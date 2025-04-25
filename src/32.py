import math

def find_closest_value(numbers, target):
    closest_value = min(numbers, key=lambda x: abs(x - target))
    return closest_value

numbers = [1, 2, 4, 5, 7, 9]
target = 6
print(find_closest_value(numbers, target))  # Output: 4
