# # розминка з подвійним for loop
# # порівняння list та tuple
# # змінні не змінні типи даних різниця
# # методи строк(split(), rsplit(), join())
# # методи list(append(), pop(), sort(), copy())
# # функція sorted()
#
#
#
# # list() tuple()
#
#
# # value_tuple = ('string', 1, 1.5, None, [])
# #
# # value_list = ['string', 1, 1.5, None, []]
# #
# # # print(value_list, type(value_list))
# #
# # new_value = tuple(value_list)
# # # print(new_value, type(new_value))
# #
# # value = 'hello'
# #
# # print(list(value))
#
# value_list = []
# # value_list = list()
#
# ############################################
#
# # base_list = [1, 2, 3]
# # my_new_list = base_list * 4
# # print(my_new_list)
# # base_list[0] = 10
# # print(f"base_list {base_list}")
# # print(f"my_new_list {my_new_list}")
#
# ######################################
# # base_list = [1, 2, 3]
# # new_list = [base_list.copy()] * 4
# # print(new_list)
# # base_list[0] = 10
# # print(f"base_list {base_list}")
# # print(f"new_list {new_list}")
# # ######################################
#
#
# # base_list = [1, 2, 3]
#
# # print(base_list)
#
# # base_list[0] = ["kkkk"]
#
# # print(base_list)
#
# # base_list.append('Hello')
# # # base_list.insert(1, 'Hello')
# # base_list.pop()
# #
# # print(base_list)
# #
# # websites = [
# #     "www.site1.com",
# #     "www.site2.com",
# #     "www.site3.com",
# #     "www.site4.com",
# #     "www.site5.com",
# #     "www.site6.com",
# #     "www.site7.com",
# #     "www.site8.com",
# #     "www.site9.com",
# # ]
# #
# # while len(websites):
# #     web = websites.pop()
# # #     print(web)
# # #
# # # print(websites)
# #
# #
# # value_list = [
# #     'hello',
# # ]
# # value_tuple = (
# #     'hello',
# # )
# #
# # print(value_list, type(value_list))
# # print(value_tuple, type(value_tuple))
#
#
#
# ########## split rplit join ##########
#
#
# # value = "Desctop/Documents/home/img_01.jpg"
# #
# # value_list = value.rsplit("/")
# # value_list[-1] = 'png'
# # print(value_list)
# #
# # value_join = ".".join(value_list)
# # print(value_join)
# # value = "qwerty qwerty qwerty qwerty "
# # print(value.split())
#
# ########### IndexError ########
# #
# # base_list = [1, 2, 3]
# #
# # index = 3
# #
# # if len(base_list) <= index:
# #     print(base_list[index])
#
# ########### sort
#
# # base_list = [1, 7, 5, -4, 2, 3]
# base_list = ["amp", "aamp", "aaamp", "kam", "cat", "1", "]", "@"]
#
# # new_list = base_list.sort(reverse=True)
#
# # print(base_list)
#
# new_list = sorted(base_list)
#
# # print(base_list)
# # print(new_list)
#
# # ASCII міжнародний стандарт табуляції
#
# print(ord('1'), ord('@'), ord(']'), ord('a'), ord('m'))
#
# print(chr(97))
#
