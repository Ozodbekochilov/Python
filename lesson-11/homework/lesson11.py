
# --TASK-2
# Create custom modules.

# math_operations.py
# Define add, subtract, multiply and divide functions (all take 2 arguments)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"







# --TASK-3
# string_utils.py
# Define reverse_string and count_vowels functions (both take 1 argument)

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)




# --TASK-4
# Create custom packages.

# geometry package structure:
# geometry/
#     __init__.py
#     circle.py

# File: geometry/__init__.py
# (Leave this file empty or just add a comment)
# This makes 'geometry' a Python package

# File: geometry/circle.py
# Define calculate_area and calculate_circumference (1 argument: radius)

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


# --TASK-5
# file_operations package structure:
# file_operations/
#     __init__.py
#     file_reader.py
#     file_writer.py

# File: file_operations/__init__.py
# (Leave empty or add a comment)
# Makes 'file_operations' a package

# File: file_operations/file_reader.py

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found."

# File: file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
