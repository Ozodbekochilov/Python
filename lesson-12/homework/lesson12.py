# --TASK-1
#  Exercise 1: Threaded Prime Number Checker
import threading

# Tub sonni tekshiruvchi funksiya
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Oqim bajaradigan funksiya
def check_primes(start, end, result):
    for number in range(start, end):
        if is_prime(number):
            result.append(number)

# Asosiy dastur
if __name__ == "__main__":
    start_range = 1
    end_range = 1000
    num_threads = 4

    thread_list = []
    results = [[] for _ in range(num_threads)]

    range_per_thread = (end_range - start_range) // num_threads

    for i in range(num_threads):
        thread_start = start_range + i * range_per_thread
        thread_end = thread_start + range_per_thread
        if i == num_threads - 1:
            thread_end = end_range  # oxirgi threadga qolganini beramiz

        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, results[i]))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    # Natijalarni birlashtirish
    all_primes = []
    for sublist in results:
        all_primes.extend(sublist)

    print("Topilgan tub sonlar:")
    print(sorted(all_primes))

# --Uzim qilmadim CHATgpt dan oldim javobini




# --TASK-2
# Exercise 2: Threaded File Processing
import threading
from collections import defaultdict

# Har bir thread uchun matnni qayta ishlovchi funksiya
def process_lines(lines, word_count_dict):
    for line in lines:
        words = line.strip().lower().split()
        for word in words:
            word = word.strip('.,!?";:()[]')  # belgilarni olib tashlash
            if word:
                with lock:
                    word_count_dict[word] += 1

# Asosiy dastur
if __name__ == "__main__":
    file_path = "large_text_file.txt"  # Fayl nomi
    num_threads = 4
    lock = threading.Lock()

    # Faylni o‘qish
    with open(file_path, "r", encoding="utf-8") as f:
        all_lines = f.readlines()

    total_lines = len(all_lines)
    lines_per_thread = total_lines // num_threads
    word_counts = defaultdict(int)

    threads = []

    for i in range(num_threads):
        start_index = i * lines_per_thread
        end_index = (i + 1) * lines_per_thread if i != num_threads - 1 else total_lines
        thread_lines = all_lines[start_index:end_index]

        t = threading.Thread(target=process_lines, args=(thread_lines, word_counts))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Natijalarni chiqarish
    print("So‘zlar uchrashi (Word Counts):")
    for word, count in sorted(word_counts.items(), key=lambda x: -x[1])[:20]:  # faqat eng ko‘p uchragan 20 ta
        print(f"{word}: {count}")
