# --TASK-1
# --QILIB BILMADIM  :)



# --TASK-2
n = int(input("Enter a number: "))
for i in range(n):
    print(i**2)



# --TASK-3
# Exercise 1:
i = 1
while i <= 10:
    print(i)
    i += 1


# Exercise 2:
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


# Exercise 3:
num = int(input("Enter number: "))
total = 0
for i in range(1, num+1):
    total += i
print("Sum is:", total)


# Exercise 4:
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)


# Exercise 5:
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)


# Exercise 6:
num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits:", count)


# Exercise 7:
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()


# Exercise 8:
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)



# Exercise 9:
for i in range(-10, 0):
    print(i)


# Exercise 10:
for i in range(5):
    print(i)
print("Done!")


# Exercise 11:
start = 25
end = 50
print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)


# Exercise 12:
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b


# Exercise 13:
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")




# --TASK-4
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for item in (c1 - c2).elements():
        result.append(item)
    for item in (c2 - c1).elements():
        result.append(item)
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))           # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))           # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))# [2, 2, 5]


