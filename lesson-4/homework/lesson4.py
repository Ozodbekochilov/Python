# --TASK-1
# --Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.
data = {3: 15, 1: 5, 2: 10}

sorted_asc = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_asc)

sorted_desc = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
print(sorted_desc)



# --TASK-2
# --Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
d = {0: 10, 1: 20}
d[2] = 30

print(d)



# --TASK-3
# --Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dic = dic1.copy()
new_dic.update(dic2)
new_dic.update(dic3)

print(new_dic)



# --TASK-4
# --Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5
squares = {}

for i in range(1, n+1):
    squares[i] = i * i

print(squares)



# --TASK-5
# --Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
squares = {}

for i in range(1, 16):
    squares[i] = i * i

print(squares)



# --TASK-6
# --Create a Set
# Write a Python program to create a set.
my_set = {1, 2, 3}

print(my_set)



# --TASK-7
# --Iterate Over a Set
# Write a Python program to iterate over sets
for item in my_set:
    print(item)



# --TASK-8
# --Add Member(s) to a Set
# Write a Python program to add member(s) to a set.
my_set.add(4)  
my_set.update([5, 6])

print(my_set)



# --TASK-9
# --Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
my_set.remove(2) 

print(my_set)



# --TASK-9
# --Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.
if 3 in my_set:
    my_set.remove(3)
    
print(my_set)



