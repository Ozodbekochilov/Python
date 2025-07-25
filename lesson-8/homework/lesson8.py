# --TASK-1
# Task: Write a Python program to handle a ZeroDivisionError when dividing a number by zero.

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")



# --TASK-2
# Task: Prompt the user to enter an integer and handle ValueError if the input is invalid.
try:
    number = int(input("Enter an integer: "))
    print(f"You entered: {number}")
except ValueError:
    print("Error: That is not a valid integer!")



# --TASK-3
# Task: Open a file and handle FileNotFoundError if the file does not exist.
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found!")



# --TASK-4
# Task: Prompt the user to enter two numbers and raise TypeError if the inputs are not numeric.
a = input("Enter first number: ")
b = input("Enter second number: ")

if not (a.isdigit() and b.isdigit()):
    raise TypeError("Error: Inputs must be numeric!")
else:
    print(int(a) + int(b))



# --TASK-5
# Task: Open a file and handle PermissionError if there is a permission issue.
try:
    f = open("/root/secret.txt", "r")
except PermissionError:
    print("Error: Permission denied!")



# --TASK-6
# Task: Perform an operation on a list and handle IndexError if the index is out of range.
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: Index out of range!")



# --TASK-7
# Task: Prompt the user to enter a number and handle KeyboardInterrupt if the input is cancelled.
try:
    num = input("Enter a number (don't press Ctrl+C): ")
    print(f"You entered: {num}")
except KeyboardInterrupt:
    print("\nError: Input cancelled by user.")



# --TASK-8
# Task: Perform a division and handle any ArithmeticError.
try:
    x = 10
    y = 0
    print(x // y)
except ArithmeticError:
    print("Error: Arithmetic operation failed.")



# --TASK-9
# Task: Open a file and handle UnicodeDecodeError if there is an encoding issue.
try:
    with open("file.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Error: Unicode decoding failed.")



# --TASK-10
# Task: Perform a list operation and handle AttributeError if the attribute doesn't exist.
try:
    lst = [1, 2, 3]
    lst.upper()
except AttributeError:
    print("Error: Attribute does not exist on list.")



# --TASK-11
# Task: Read an entire text file.
with open("sample.txt", "r") as f:
    print(f.read())



# --TASK-12
# Task: Read the first n lines of a file.
n = 3
with open("sample.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")



# --TASK-13
# Task: Append text to a file and display the content.
with open("sample.txt", "a") as f:
    f.write("\nNew line added.")

with open("sample.txt", "r") as f:
    print(f.read())



# --TASK-14
# Task: Read the last n lines of a file.
n = 2
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))



# --TASK-15
# Task: Read a file line by line and store it into a list.
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(lines)



# --TASK-16
# Task: Read a file line by line and store it into a variable.
with open("sample.txt", "r") as f:
    content = f.read()
print(content)



# --TASK-17
# Task: Read a file line by line and store it into an array.
with open("sample.txt", "r") as f:
    arr = [line.strip() for line in f]
print(arr)



# --TASK-18
# Task: Find the longest word(s) in a file.
with open("sample.txt", "r") as f:
    words = f.read().split()
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]
print(longest)



# --TASK-19
# Task: Count the number of lines in a text file.
with open("sample.txt", "r") as f:
    count = sum(1 for _ in f)
print("Total lines:", count)



# --TASK-20
# Task: Count the frequency of words in a file.
from collections import Counter

with open("sample.txt", "r") as f:
    words = f.read().split()
    freq = Counter(words)
print(freq)



# --TASK-21
# Task: Get the file size of a plain file.
import os
print(os.path.getsize("sample.txt"), "bytes")



# --TASK-22
# Task: Write a list to a file.
items = ['apple', 'banana', 'cherry']
with open("list.txt", "w") as f:
    for item in items:
        f.write(item + "\n")



# --TASK-23
# Task: Copy the contents of a file to another file.
with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())



# --TASK-24
# Task: Combine each line from the first file with the corresponding line in the second file.
with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())



# --TASK-25
# Task: Read a random line from a file.
import random
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(random.choice(lines))



# --TASK-26
# Task: Check if a file is closed or not.
f = open("sample.txt", "r")
print("Closed:", f.closed)
f.close()
print("Closed:", f.closed)



# --TASK-27
# Task: Remove newline characters from a file.
with open("sample.txt", "r") as f:
    clean_lines = [line.strip() for line in f]
print(clean_lines)



# --TASK-28
# Task: Return the number of words in a file. (Note: words may be separated by commas with no space)
with open("sample.txt", "r") as f:
    text = f.read().replace(',', ' ')
    words = text.split()
print("Word count:", len(words))



# --TASK-29
# Task: Extract characters from multiple text files and store them in a list.
import glob

chars = []
for file in glob.glob("*.txt"):
    with open(file, "r") as f:
        chars.extend(list(f.read()))
print(chars)



# --TASK-30
# Task: Generate 26 text files named A.txt, B.txt, ..., Z.txt.
import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt\n")



# --TASK-31
# Task: Create a file listing all English alphabet letters with a specified number of letters per line.
letters = string.ascii_lowercase
n = 5
with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write(letters[i:i+n] + "\n")
