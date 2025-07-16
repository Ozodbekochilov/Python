# --TASK-1
def is_leap(year):
    if not isinstance(year, int):
        raise ValueError("Yil butun son bo'lishi kerak.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap(2020))
print(is_leap(1900))
print(is_leap(2000))



# --TASK-2
n = int(input("Sonni kiriting: "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")



# --TASK-3
def even_numbers_between(a, b):
    if a % 2 != 0:
        a += 1  # juft sonlardan boshlaymiz
    return list(range(a, b+1, 2))

print(even_numbers_between(3, 10))  # [4, 6, 8, 10]
