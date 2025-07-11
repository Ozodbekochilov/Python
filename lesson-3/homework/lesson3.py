#--TASK-1
#Create and Access List Elements
#Create a list containing five different fruits and print the third fruit.
fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']

print(fruits[2])  # Output: cherry



#--TASK-2
#Concatenate Two Lists
#Create two lists of numbers and concatenate them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2

print(combined_list)



# --TASK-3
# Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [10, 20, 30, 40, 50]
new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]

print(new_list)



# --TASK-4
# Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
movies = ['Inception', 'Interstellar', 'Matrix', 'Avatar', 'Gladiator']
movies_tuple = tuple(movies)

print(movies_tuple)




# --TASK-5
# Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['London', 'New York', 'Paris', 'Tokyo']

print("Paris" in cities) 



# --TASK-6
# Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3]
duplicated = numbers * 2

print(duplicated)



# --TASK-7
# Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]

print(nums)



# --TASK-8
# Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = tuple(range(1, 11))
print(numbers[3:8])



# --TASK-9
# Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.
colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
count_blue = colors.count('blue')

print(count_blue)  # Output: 3



# --TASK-10
# Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".
animals = ('dog', 'cat', 'lion', 'tiger')
index = animals.index('lion')

print(index)  # Output: 2




# --TASK-11
# Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2

print(merged)  



# --TASK-12
# Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30]
my_tuple = (1, 2, 3, 4)

print(len(my_list)) 
print(len(my_tuple))



# --TASK-13
# Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
num_tuple = (5, 10, 15, 20, 25)
num_list = list(num_tuple)

print(num_list) 



# --TASK-14
# Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (8, 3, 15, 1, 10)

print(max(numbers)) 
print(min(numbers)) 



# --TASK-15
# Reverse a Tuple
# Given a tuple, reverse it.
my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)  # Output: (5, 4, 3, 2, 1)
