def calculate_circle_area(radius):
    """Calculate the area of a circle"""
    return 3.14 * radius ** 2

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle"""
    return 0.5 * base * height

shape = input("Enter the shape (circle, rectangle, triangle): ")

if shape == "circle":
    radius = float(input("Enter the radius: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle is {area}")

elif shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is {area}")

elif shape == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle is {area}")

else:
    print("Invalid shape. Please try again.")
