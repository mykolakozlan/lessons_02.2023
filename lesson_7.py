# practice
# list comprehension
# sets
# sets methods(union(), difference(), intersection())

################################################
# Ви маєте змінну my_str, тип - str. Надрукувати ЧИСЛО скільки РІЗНИХ символів зустрічається в my_str.
# Велика та маленька літера вважається одним символом. Пробіл, коми і т.д. вважаємо також як символи.
# Наприклад: my_str="bla BLA car"
#            Виведення на екран: 6

# my_str = "bla BLA car"
# value_list = []
# value_str = ""
# result = 0
#
# for x in my_str.lower():
#     print(value_str)
#     if x not in value_str:
#         # value_list.append(x)
#         value_str += x
#
# result = len(value_str)
# print(result)


# my_string = list("bla BLA car".lower())
# value_list = []
# start = -1
#
# while len(my_string):
#     symb = my_string.pop()
#     if symb not in value_list:
#         value_list.append(symb)
# print(len(value_list))


################################################
# Ви маєте змінну my_str, та порожній список my_list. Заповнити my_list УНІКАЛЬНИМИ символами з my_str.
# Велика та маленька літера вважається одним символом. Пробіл, коми і т.д. вважаємо також як символи.
# Наприклад: my_str = "bla BLA car"
#            Виведення на екран: ["b", "l", "a", " ", "c", "r"]

# my_str = "bla BLA car"
# value_list = []
# print(id(value_list))
#
# for x in my_str.lower():
#     if x not in value_list:
#         value_list.append(x)
#         # value_list = value_list + list(x)
#         # value_list += list(x)
#
# print(value_list, id(value_list))



################################################
# Дано рядок my_str та порожній список my_list. Заповнити my_list символами з my_str,
# які стоять на парних місцях у рядку (вважаємо з 0)
# Наприклад: my_str = "bla BLA car"
#            Виведення на екран: ["b", "a", "B", "A", "c", "r"]

# my_str = "bla BLA car"
# my_list = []


#1
# my_list += list(my_str[::2])

#2
# for i in my_str[::2]:
#     my_list.append(i)

#3
# for i in range(0, len(my_str)):
#     if i % 2 == 0:
#         my_list.append(my_str[i])

#4
# for i in range(0, len(my_str), 2):
#     my_list.append(my_str[i])

# print(my_list)


################################################
# Дано рядок my_str, список str_index цілих чисел в діапазоні від 0 до довжини рядка мінус 1,
# пустий список my_list. Заповнити my_list символами my_str, які стоять на місцях з
# індексами із str_index
# Наприклад: key = "bla BLA car"
#            str_indexes = [0, 2, 4, 4, 8]
#            Виведення на екран: ["b", "a", "B", "B", "c"]

# my_str = "bla BLA car"
# str_indexes = [0, 2, 4, 4, 8]
#
# my_list = []
#
# for index in str_indexes:
#     my_list.append(my_str[index])
#
# print(my_list)



################################################
# Дано ціле число (int). Визначити скільки цифр у цьому числі.
# Наприклад: my_number = 228989
#            Виведення на екран: 6
#
# my_num = input("Give me a number:")
# my_strange = str(my_num)
# ln = len(my_strange)
# print(ln)


# Дано ціле число. Визначити найбільшу цифру у цьому числі.
# Наприклад: my_number = 228989
#            Виведення на екран: 9


#1
# my_number = 22882
# my_list = list(str(my_number))
# my_list.sort()
#
# print(my_list[-1])

# 2
# my_number = 228989
# sorted_my_number = sorted(str(my_number))
# print(sorted_my_number[-1])
#

# my_number = "228989ma"
# # ASCII
# result = max(my_number)
# print(result)

#
# Дано ціле число. Скласти число (int) із цифрами у зворотному порядку.
# Наприклад: my_number = 1263
#            Виведення на екран: 3621

# my_number = 1263
# res = str(my_number)[::-1]
# # s = "22132sdaasas2//:-."
# # print (''.join(sorted([n for n in set(s) if n.isdigit()], reverse=True)))
#
# print(int(res))


# my_number = 123
# my_list = list(str(my_number))
# sorted_my_number = sorted(my_list, reverse=True)
# reverse_my_value = ''
# for i in sorted_my_number:
#     reverse_my_value += i
# print(reverse_my_value)

#
#
# Дано ціле число. Скласти число з цифрами в порядку зростання (зменшення).
# Наприклад: my_number = 3254
#            Виведення на екран: 2345   #зростання
#            Виведення на екран: 5432   #зменшення

# my_number = 3254
#1
# s = "123456"
# print (''.join(sorted([n for n in set(s) if n.isdigit()], reverse=True)))

#2
# my_number = 3254
# my_list = list(str(my_number))
#
# my_list.sort()
# new_number1 = ''.join(my_list)
# print(new_number1)
#
# my_list.sort(reverse=True)
# new_number2 = ''.join(my_list)
# print(new_number2)

# #3
# my_number = 3254
# my_list = list(str(my_number))
# sorted_my_number = sorted(my_list)
# my_result = ''
# for i in sorted_my_number:
#     my_result += i
# print(my_result)
#
# sorted_my_number_reverse = sorted(my_list, reverse=True)
# my_result_reverse = ''
# for i in sorted_my_number_reverse:
#     my_result_reverse += i
# print(my_result_reverse)

################################################
# Дано списки my_list_1 та my_list_2. Створити список my_result в який помістити елементи
# з my_list_1 та my_list_2 через один, починаючи з my_list_1.
# a) кількість ел-тів однакове
# б) кількість ел-тів різне
# Наприклад: my_list_1 = [1, 2, 3]
#            my_list_2 = [10, 20, 30] # для варінту a
#            my_list_2 = [10, 20, 30, 40] # для варінту б
#            Виведення на екран: [1, 10, 2, 20, 3, 30]   #ел-тів однакове
#            Виведення на екран: [1, 10, 2, 20, 3, 30, 40]   #ел-тів різне


# #1
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 50, 40, 60]
#
# result_1 = []
#
# my_list_1.reverse()
# my_list_2.reverse()
#
# if len(my_list_1) >= len(my_list_2):
#     while len(my_list_1):
#         num_1 = my_list_1.pop()
#         num_2 = my_list_2.pop()
#         result_1.append(num_1)
#         result_1.append(num_2)
# else:
#     while len(my_list_1):
#         num_1 = my_list_1.pop()
#         num_2 = my_list_2.pop()
#         result_1.append(num_1)
#         result_1.append(num_2)
#     while len(my_list_2):
#         num_2 = my_list_2.pop()
#         result_1.append(num_2)
#
# print(result_1)

#2
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30]
# my_result = []
# index_count = 0
# while index_count <= len(my_list_2) + 1:
#     try:
#         my_result.append(my_list_1.pop(0))
#         my_result.append(my_list_2.pop(0))
#         index_count += 1
#     except IndexError:
#         break
# print(my_result)
#
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30, 40, 60]
#
# result_1 = []


#3
# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 50, 70, 80]
# result = []
#
# index_val = min(len(my_list_1), len(my_list_2))
#
# for i in range(index_val):
#     result.append(my_list_1[i])
#     result.append(my_list_2[i])
#
# # result += my_list_1[index_val:]
# # result += my_list_2[index_val:]
#
#
# result.extend(my_list_1[index_val:])
# result.extend(my_list_2[index_val:])
#
# print(result)


################################################
