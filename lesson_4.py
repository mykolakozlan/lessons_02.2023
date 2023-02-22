# 3 stages of programming

# if statement not
# ternary operator
# while (True, flag, value)
# break, continue
# while else
# str methods

# value = False

# and, or, not

# if (value == "+") or (value == "-"):
#     print("!!!!")
# else:
#     print("????")

# if not value:  # value == False
#     print("8888")

# value_int = 10
#
# # if (value_int % 2) == 0 and (value_int % 5) == 0:
# if not (value_int % 2) and not (value_int % 5):
#     print(value_int)

# value = input("type somthng:")
# # #
# # # if not value:
# # #     print("no value")
# # # else:
# # #     print("have value")


############## ternary operator #############

#
# value = 1
# # if value > 0:
# #     result = True
# # else:
# #     result = False
# #     # print("")
#
# result = 10 if value > 0 else 15
#
# print(result)

######### while (True, flag, value) #########

# value = 1
# flag = True

# while True:
#     value += 1  # value = value + 1
#     print(value)


# while value < 10:
#     value += 1  # value = value + 1
#     print(value)

# while is_true:
#     value += 1  # value = value + 1
#     print(value)
#     if value > 10:
#         is_true = False
#
# print("end")

# while flag:
#     try:
#         value = int(input("ll"))
#
#         flag = False
#
#     except:
#         print("error")

# value_1 = 0
#
# while value_1 > 10:
#     try:
#         value_1 = int(input("ll"))
#
#         # flag = False
#
#     except:
#         print("error")
#
# print(value_1)
#
# while True:
#     try:
#         value_1 = int(input("ll"))
#         break
#     except:
#         print("error")

# value = 1
#
# while value < 10:
#     value += 1
#     if not(value % 2):
#         continue
#     print(value)
#
# # continue
#
# print("end")

# value = 1
#
# while value < 10:
#     value += 1
#     if not(value % 2):
#         continue
#     print(value)
# else:
#    print(value)

# print(value)


#########str methods########

# value = "qu/e{&"
#
# index = 20
# if len(value) >= index:
#     print(value[index])  # виклик за індексом
# else:
#     print("string index out of range")
# print(value[1:2:1])  # перший елемент - з чогось, другий - до чогось, третій - крок

# print(value[1:4])  # від включно, до виключно
# print(value[2:3])  # від включно, до виключно
# print(value[::-1])
# print(value[:20:1])
# print(value[::2]) #виклик нечотних
# print(value[1::2]) #виклик чотних

# len() визначає довжину об'єкту

# print(len(value))

# value = 20
#
# if str(value)[0] == "2":
#     print("yes")
#

# value_1 = "nikolas"
# # value_2 = input("type")
# # if value_1.lower() == value_2.lower():
#
#     # print(value_1)
#
# # print(value_1.lower()) #нижній регістр
# # print(value_1.upper()) #верхній регістр
# # print(value_1.capitalize()) #першу літеру в верхній регістр
#
# txt = "document.txt"
#
# x = txt.find(".")
# print(x)
# value_length = len(txt)
# print(value_length)
# print(txt[(x - value_length + 1):])
# print(txt[(txt.find(".")+1)::])
