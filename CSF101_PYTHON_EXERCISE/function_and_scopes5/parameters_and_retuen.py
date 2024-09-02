#6
def greet_with_default(name = "guest"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("bob")

#7
def calculate_rectangle_area(width, height):
    return width * height
area = calculate_rectangle_area(5, 3)
print(f"The area of the rectangle is : {area}")

#8
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    
print_info("Jigme", age=18, city="Gedu")

#9
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([5, 2, 8, 1, 9])
print(f"min: {result[0]}, max: {result[1]}")

#10
def safe_divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a/b

