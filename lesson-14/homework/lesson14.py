# ==============================
# --task-1
# --JSON Parsing: students.json faylini o‘qib, har bir talabaning ma’lumotlarini chiqarish.
import json

try:
    with open("students.json", "r", encoding="utf-8") as f:
        students = json.load(f)

    for student in students:
        print(f"Ismi: {student.get('name')}, Yoshi: {student.get('age')}, Kursi: {student.get('course')}")
except FileNotFoundError:
    print("students.json fayli topilmadi.")
except json.JSONDecodeError:
    print("JSON formatida xatolik bor.")



# ==============================
# --task-2
# --Weather API: Tashkent shahri bo‘yicha ob-havo ma’lumotlarini OpenWeatherMap dan olish.
import requests

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # OpenWeatherMap saytida ro'yxatdan o'tib olish kerak
city = "Tashkent"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Shahar: {data['name']}")
        print(f"Harorat: {data['main']['temp']}°C")
        print(f"Namlik: {data['main']['humidity']}%")
        print(f"Holat: {data['weather'][0]['description']}")
    else:
        print("Xato:", data.get("message", "Ma'lumot topilmadi"))
except requests.RequestException:
    print("Tarmoq bilan bog‘liq xatolik yuz berdi.")



# ==============================
# --task-3
# --JSON Modification: books.json faylida kitob qo‘shish, yangilash va o‘chirish funksiyalari.
import json
import os

books_file = "books.json"

# Fayl bo‘lmasa, bo‘sh ro‘yxat yaratish
if not os.path.exists(books_file):
    with open(books_file, "w", encoding="utf-8") as f:
        json.dump([], f)

def load_books():
    with open(books_file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(books_file, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4)

def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print("Kitob qo‘shildi.")

def update_book(old_title, new_title, new_author):
    books = load_books()
    for book in books:
        if book["title"] == old_title:
            book["title"] = new_title
            book["author"] = new_author
            save_books(books)
            print("Kitob yangilandi.")
            return
    print("Kitob topilmadi.")

def delete_book(title):
    books = load_books()
    books = [book for book in books if book["title"] != title]
    save_books(books)
    print("Kitob o‘chirildi.")



# Misol uchun:
# add_book("Python Asoslari", "Ali Valiyev")
# update_book("Python Asoslari", "Python Professional", "Ali Valiyev")
# delete_book("Python Professional")

# ==============================
# --task-4
# --Movie Recommendation System: OMDb API yordamida janr bo‘yicha random film tavsiya qilish.
import requests
import random

OMDB_API_KEY = "YOUR_OMDB_API_KEY"  # OMDb API saytida ro'yxatdan o'tib olish kerak
genre = input("Film janrini kiriting (masalan: Action, Comedy, Drama): ")

url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&type=movie&s={genre}"

try:
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        movies = data.get("Search", [])
        if movies:
            random_movie = random.choice(movies)
            print(f"Tavsiya etilgan film: {random_movie['Title']} ({random_movie['Year']})")
        else:
            print("Bu janr bo‘yicha film topilmadi.")
    else:
        print("Xato:", data.get("Error", "Ma'lumot topilmadi."))
except requests.RequestException:
    print("Tarmoq bilan bog‘liq xatolik yuz berdi.")
