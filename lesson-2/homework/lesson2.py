# TASk-1
# Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
ism = input('Ismingizni Kiriting: ')
yil = int(input('Yilingizni Kiriting: '))
yosh = 2025 - yil

print(f'Assalomu aleykum {ism}, Szning yowingiz {yosh} da')



# TASK-2
# Extract Car Names
# Extract car names from the following text:
txt = 'LMaasleitbtui'
car1 = txt[::2]
car2 = txt[1::2]  

print(car1)
print(car2)


# TASK-3
# Extract Car Names
# Extract car names from the following text:
txt = 'MsaatmiazD'
car_name = txt[0] + txt[2] + txt[8] + txt[9].lower() + txt[4]
print("Ajratilgan mashina nomi:", car_name) 



# TASK-4
# Extract Residence Area
# Extract the residence area from the following text:
txt = "I'am John. I am from London"
area = txt.split("from")[-1].strip()
print("Yashash joyi:", area)



# TASK-5
# Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.
text = input("Matn kiriting: ")
print("Teskari matn:", text[::-1])



# TASK-6
# Count Vowels
# Write a Python program that counts the number of vowels in a given string.
text = input("Matn kiriting: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Unli harflar soni:", count)



# TASK-7
# Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
nums = input("Sonlarni vergul bilan kiriting (masalan: 3,7,1,9): ")
num_list = [int(n) for n in nums.split(',')]
print("Eng katta qiymat:", max(num_list))



# TASK-8
# Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
word = input("So‘z kiriting: ")
if word == word[::-1]:
    print("Bu so‘z palindrom.")
else:
    print("Bu so‘z palindrom emas.")



# TASK-9
# Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Email manzilini kiriting: ")
domain = email.split('@')[-1]
print("Domen:", domain)



# TASK-10
# Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

length = 12  # Parol uzunligi
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Tasodifiy parol:", password)


