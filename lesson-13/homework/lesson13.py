# ==============================
# --task-1
# --Age Calculator: Foydalanuvchidan tug‘ilgan sanasini so‘rab, yoshi yillar, oylar va kunlarda hisoblab chiqarish.
from datetime import datetime

birthdate_str = input("Tug'ilgan sanangizni kiriting (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += (today.replace(month=today.month, day=1) - datetime(today.year, today.month - 1, 1)).days

if months < 0:
    years -= 1
    months += 12

print(f"Siz {years} yil, {months} oy va {days} kunliksiz.")

# ==============================
# --task-2
# --Days Until Next Birthday: Keyingi tug‘ilgan kuningizgacha qolgan kunlarni hisoblash.
from datetime import datetime, timedelta

birthdate_str = input("Tug'ilgan sanangizni kiriting (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_remaining = (next_birthday - today).days
print(f"Keyingi tug‘ilgan kuningizgacha {days_remaining} kun qoldi.")

# ==============================
# --task-3
# --Meeting Scheduler: Hozirgi sana/vaqt va uchrashuv davomiyligi kiritilganda uchrashuv tugash vaqtini hisoblash.
from datetime import datetime, timedelta

current_str = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
duration_hours = int(input("Uchrashuv davomiyligi (soat): "))
duration_minutes = int(input("Uchrashuv davomiyligi (daqiqa): "))

current_datetime = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
end_time = current_datetime + timedelta(hours=duration_hours, minutes=duration_minutes)

print(f"Uchrashuv tugash vaqti: {end_time}")

# ==============================
# --task-4
# --Timezone Converter: Sana/vaqtni bitta vaqt zonasidan boshqasiga aylantirish.
from datetime import datetime
import pytz

date_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_tz_str = input("Hozirgi vaqt zonangizni kiriting (masalan: Asia/Tashkent): ")
to_tz_str = input("O‘zgartirmoqchi bo‘lgan vaqt zonasi (masalan: Europe/London): ")

from_tz = pytz.timezone(from_tz_str)
to_tz = pytz.timezone(to_tz_str)

local_dt = from_tz.localize(datetime.strptime(date_str, "%Y-%m-%d %H:%M"))
converted_dt = local_dt.astimezone(to_tz)

print(f"Natija: {converted_dt}")

# ==============================
# --task-5
# --Countdown Timer: Kelajakdagi sanagacha qolgan vaqtni har sekundda chiqarish.
from datetime import datetime
import time

future_str = input("Kelajakdagi sana va vaqt (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = future_time - now
    if remaining.total_seconds() <= 0:
        print("Vaqt tugadi!")
        break
    print(f"Qolgan vaqt: {remaining}")
    time.sleep(1)

# ==============================
# --task-6
# --Email Validator: Email manzilini format bo‘yicha tekshirish.
import re

email = input("Email kiriting: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Email to‘g‘ri formatda.")
else:
    print("Email xato formatda.")

# ==============================
# --task-7
# --Phone Number Formatter: Telefon raqamini standart formatga o‘tkazish.
phone = input("Telefon raqamingizni kiriting (faqat raqamlar): ")

if len(phone) == 10 and phone.isdigit():
    formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatlangan raqam:", formatted_phone)
else:
    print("Xato raqam kiritildi.")

# ==============================
# --task-8
# --Password Strength Checker: Parol kuchini tekshirish.
import re

password = input("Parol kiriting: ")

length_ok = len(password) >= 8
uppercase_ok = bool(re.search(r'[A-Z]', password))
lowercase_ok = bool(re.search(r'[a-z]', password))
digit_ok = bool(re.search(r'\d', password))

if length_ok and uppercase_ok and lowercase_ok and digit_ok:
    print("Parol kuchli.")
else:
    print("Parol kuchsiz. Talablar: kamida 8 belgidan iborat, bitta katta harf, bitta kichik harf va bitta raqam bo‘lishi kerak.")

# ==============================
# --task-9
# --Word Finder: Berilgan matnda so‘zni qidirish va barcha uchrashuvlarini chiqarish.
text = """Python is great. Python is easy to learn. Many people love Python."""
word = input("Qidiriladigan so‘zni kiriting: ")

matches = [m.start() for m in re.finditer(word, text)]
if matches:
    print(f"So‘z {len(matches)} marta topildi, joylashuvlari: {matches}")
else:
    print("So‘z topilmadi.")

# ==============================
# --task-10
# --Date Extractor: Matndan sanalarni topish.
text = input("Matn kiriting: ")
pattern = r'\b\d{4}-\d{2}-\d{2}\b'

dates = re.findall(pattern, text)
if dates:
    print("Topilgan sanalar:", dates)
else:
    print("Sana topilmadi.")
