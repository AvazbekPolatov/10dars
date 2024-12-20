# # Faylga masala raqamlari bilan yozish

import os
from multiprocessing import Process, Manager
#
# def read_file(filepath, result):
#     if not os.path.exists(filepath):
#         result.append(f"Fayl topilmadi: {filepath}")
#         return
#     with open(filepath, 'r') as file:
#         content = file.read()
#     result.append(content)
#
# def read_file_multiprocessing(filepath):
#     manager = Manager()
#     result = manager.list()
#     process = Process(target=read_file, args=(filepath, result))
#     process.start()
#     process.join()
#     return list(result)[0]
#
# if __name__ == "__main__":
#     file_path = 'file.txt'
#     content = read_file_multiprocessing(file_path)
#     print(content)
#

import multiprocessing


# Parallel ishni bajarish uchun yordamchi funksiya
def parallel_function(func, data):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(func, data)


# 1. Raqamlar yig'indisi
def sum_numbers(numbers):
    total = sum(numbers)
    print(f"Raqamlar yig'indisi: {total}")


# 2. Ro'yxatni aylantirish
def rotate_list(lst):
    rotated = lst[1:] + [lst[0]]
    print(f"Ro'yxatni aylantirish: {rotated}")


# 3. Minimal va maksimal qiymatlarni topish
def min_max(numbers):
    result = (min(numbers), max(numbers))
    print(f"Minimal va maksimal qiymatlar: {result}")


# 4. Elementni qidirish
def find_element(args):
    lst, value = args
    found = value in lst
    print(f"Element {value} ro'yxatda {'topildi' if found else 'topilmadi'}")


# 5. Ro'yxatdagi takrorlanuvchi elementlarni olib tashlash
def remove_duplicates(lst):
    unique_lst = list(set(lst))
    print(f"Takrorlanuvchi elementlar olib tashlandi: {unique_lst}")


# 6. So'zlarni teskari aylantirish
def reverse_words(words):
    reversed_words = [word[::-1] for word in words]
    print(f"So'zlarni teskari aylantirish: {reversed_words}")


# 7. Ro'yxatdagi eng uzun so'zni topish
def longest_word(words):
    longest = max(words, key=len)
    print(f"Eng uzun so'z: {longest}")


# 8. Lug‘atdagi qiymatlar orasidan takrorlangan qiymatlarni aniqlash
def find_duplicates_in_dict_values(d):
    values = list(d.values())
    seen = set()
    duplicates = set(x for x in values if x in seen or seen.add(x))
    print(f"Takrorlangan qiymatlar: {duplicates}")


# 9. Lug‘atdagi qiymatlar orasidagi barcha raqamlarni topish
def find_numbers_in_dict(d):
    numbers = [v for v in d.values() if isinstance(v, (int, float))]
    print(f"Lug'atdagi raqamlar: {numbers}")


# 10. Lug‘at qiymatlari orasida raqam bo‘lganlarini 2 ga ko‘paytiring
def multiply_numbers_in_dict(d):
    multiplied = {k: v * 2 if isinstance(v, (int, float)) else v for k, v in d.items()}
    print(f"Raqamlar 2 ga ko‘paytirildi: {multiplied}")


# 11. Lug‘atdan eng katta qiymatga ega kalitni topish
def find_max_key(d):
    # Faqat integer yoki float qiymatlarni taqqoslash
    max_key = max(d, key=lambda k: (isinstance(d[k], (int, float)), d[k]))
    print(f"Eng katta qiymatga ega kalit: {max_key}")



# 12. Lug‘atda bir nechta qiymat mavjud bo‘lsa, ularning o‘rtacha qiymatini topish
def find_average_of_multiple_values(d):
    average = {k: sum(v) / len(v) if isinstance(v, list) else v for k, v in d.items()}
    print(f"Bir nechta qiymatlar o‘rtacha: {average}")


# 13. Ikki lug‘atni birlashtirib, qiymatlar mavjud bo‘lsa ularni jamlab bitta qiymat qiling
def merge_dicts(args):
    d1, d2 = args
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            if isinstance(result[key], int) and isinstance(value, int):
                result[key] += value
            elif isinstance(result[key], str) and isinstance(value, str):
                result[key] += value
            else:
                result[key] = [result[key], value]  # Agar turlar mos kelmasa, ularni ro'yxatga qo'shamiz
        else:
            result[key] = value
    print(f"Ikki lug‘at birlashtirildi: {result}")



# 14. Lug‘atdan eng uzun va eng qisqa kalitlarni topib chiqarish
def find_longest_and_shortest_keys(d):
    keys = list(d.keys())
    shortest = min(keys, key=len)
    longest = max(keys, key=len)
    print(f"Eng uzun kalit: {longest}, Eng qisqa kalit: {shortest}")


# 15. Lug‘atdagi string qiymatlar orasida faqat raqamlar mavjud bo‘lsa, ularni raqam ko‘rinishiga aylantirish
def convert_string_values_to_numbers(d):
    converted = {
        k: int(v) if isinstance(v, str) and v.isdigit() else v
        for k, v in d.items()
    }
    print(f"Qiymatlar raqamga aylantirildi: {converted}")



# 16. Lug‘atdagi har bir qiymatni 2 ga ko‘paytirib yangi lug‘at yaratish
def multiply_values_in_dict(d):
    multiplied = {k: v * 2 for k, v in d.items()}
    print(f"Qiymatlar 2 ga ko‘paytirildi: {multiplied}")


# 17. Lug‘atdagi string qiymatlarni teskari ko‘rinishga keltirish
def reverse_string_values_in_dict(d):
    reversed_dict = {k: v[::-1] if isinstance(v, str) else v for k, v in d.items()}
    print(f"String qiymatlar teskari ko‘rinishga keltirildi: {reversed_dict}")


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]
    lst = [1, 2, 3, 4,5,6,7,8,9]
    words = ["hello", "world", "python"]
    d = {'a': '1', 'b': 2, 'c': '3', 'd': 'hello'}
    d2 = {'b': 3, 'd': 4}

    # Parallel tarzda bajarish
    parallel_function(sum_numbers, [numbers])
    parallel_function(rotate_list, [lst])
    parallel_function(min_max, [numbers])
    parallel_function(find_element, [(lst, 3)])
    parallel_function(remove_duplicates, [lst])
    parallel_function(reverse_words, [words])
    parallel_function(longest_word, [words])
    parallel_function(find_duplicates_in_dict_values, [d])
    parallel_function(find_numbers_in_dict, [d])
    parallel_function(multiply_numbers_in_dict, [d])
    parallel_function(find_max_key, [d])
    parallel_function(find_average_of_multiple_values, [d])
    parallel_function(merge_dicts, [(d, d2)])
    parallel_function(find_longest_and_shortest_keys, [d])
    parallel_function(convert_string_values_to_numbers, [d])
    parallel_function(multiply_values_in_dict, [d])
    parallel_function(reverse_string_values_in_dict, [d])

