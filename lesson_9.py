# moduls
# def



########### HW ############

# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.


def count_zeroes(num):
    num_str = str(num)
    result = num_str.count("0")
    return result


num = 100500

print(count_zeroes(num))

# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі

# num = 100500
# find_symbol = "0"
# new_list = []
# result = 0
#
# num_str = str(num)[::-1]
# print(num_str)
#
# for symbol in num_str:
#     if symbol == find_symbol:
#         result += 1
#         new_list.append(symbol)
#     else:
#         break
#
# print(new_list, len(new_list))
# print(result)
#
#
# num_str = str(num)
# result = (len(num_str) - len(num_str.rstrip(find_symbol)))
# print(result)
#
# without_zero = int(str(num)[::-1])
# result = (len(str(num)) - len(str(without_zero)))
# print(result)


# 3. Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.

# my_list_1 = ["q", "w", "e", "r", "t", "y"]
# my_list_2 = ["1", "2", "3", "4", "5", "6"]
#
# my_result = my_list_1[::2] + my_list_2[::2]
# print(my_result)

# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]

# my_list = [[1,2,3], "2", "3", "4"]
# new_list = my_list[1:] + [my_list[0]]
# print(new_list)
#
# # 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# # [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)
#
# my_list = ["one", "two", "tree", "four"]
# my_list.append(my_list.pop(0))
# print(my_list)

# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)

# test_str = "43 більше ніж 34,8y9 але менше ніж 50"
# numb_list = []
#
# # for word in test_str:
# #     if not word.isdigit():
# #         test_str.replace(word, "").split(" ")
# #
# #
# # test_str = "43       34 8 9                      50"
#
# for word in test_str.split():
#     if word.isdigit():
#         numb_list.append(int(word))
#
#     else:
#         digit = ""
#
#         for symbol in word:
#             if symbol.isdigit():
#                 digit += symbol
#             else:
#                 if digit:
#                     numb_list.append(int(digit))
#                 digit = ""
#
#
# # value_list = value.replace(",", "").split(" ")
#
# result = sum(numb_list)
# print(result)

# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.

# my_list = [8, 4, 1, 5, 3, 9, 0, 1]
# result = 0
#
# for index in range(1, len(my_list)-1):
#     if my_list[index] > my_list[index - 1] + my_list[index + 1]:
#         result += 1
#
# print(result)

# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.

# my_list = [1, 2, 3, "11", "22", 33]
# new_list = []
#
# # for value in my_list:
# #     if type(value) == str:  #isinstance(value, str)
# #         new_list.append(value)
# #
# # print(my_list)
# print(new_list)
# val_str = '11'
# # new_list.append(val_str)
# new_list += val_str
# print(new_list)


# 9. Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

# my_str = "rrrrrrhhhhauuuub"
# # res_list = []
# #
# # for symbol in set(my_str):
# #     if my_str.count(symbol) == 1:
# #         res_list.append(symbol)
# #
# # print(res_list)

# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
#
# val_set = set(my_str_1).intersection(set(my_str_2))
#
#
# res_list = list(val_set)
# print(res_list)


# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному разу

# my_str_1 = "aaaasd1ekoko212"
# my_str_2 = "asdff2"
# res_list = []
#
# for symbol in set(my_str_1).intersection(set(my_str_2)):
#     # if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
#     if my_str_1.count(symbol) + my_str_2.count(symbol) == 2:
#         res_list.append(symbol)
#
# print(res_list)
