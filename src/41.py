import math

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

# Example usage
rectangle_length = 5.0
rectangle_width = 3.0
area = calculate_area(rectangle_length, rectangle_width)
print(f"The area of the rectangle with length {rectangle_length} and width {rectangle_width} is: {area:.2f}")
