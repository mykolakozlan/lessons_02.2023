# Bool, None types
# Logic operators
# Зведення типів
# Duck typing
# If statement (programming golf, Тернарний оператор)
# input()
# working with errors



# ###### NoneType #########

# none_value = None
#
# value_int = 123
#
# print(value_int)
#
#
# value_id = id(value_int)
#
# # print(value_id, type(value_id))
#
# print_value = print(value_int)
#
# print(print_value, type(print_value))

# ###### Bool #########
#
# bool_value_1 = True
# bool_value_2 = False
#
# result_int = 2 == 2 # >, <, >=, <=, ==, !=
# result_str = "ell" in "Hello!"  # ==, !=, in
#
# print(result_str)


##### Types ########

# value_int = 11 # int
# value_str = "12.5"
#
# print(value_str, type(value_str))
#
# value_str = str(value_int)
#
# print(value_str, type(value_str))

# result = value_int + value_str
# print(result, type(result))
#
# value_int = 0
# value_float = 0.0
# value_str = ""
# value_bool = bool(value_str)
# result = bool(value_str) * 2
# print(result, type(result))
# print(bool(value_str), type(bool(value_str)))
# print(bool(value_str)*2, type(bool(value_str)*2))
# print(bool(value_str)*2)


# print(bool(value_str)*2, type(bool(value_str)*2))




######## if statement #########

#
# value = 20
# # value = "20"
#
# # if value > 0 and value < 10:     # and(+), or
#
# if 0 < value < 10:
#     print(f"{value} bigger than 0")
# elif value > 10: #else if
#     print(f"{value} bigger than 10")
# elif value < 0: #else if
#     print(f"{value} less than 0")
# else:
#     print(f"{value} is 0")
#
# print("end")


###### input() ######## ALWAYS STRING

# try:
#     value_1 = int(input("Type a number: "))
#     result = 1 / value_1
#     print(result)
# except ValueError:
#     print("Error")
# except ZeroDivisionError:
#     print("It can't a 0")
#
#
# print(99999)

# value_2 = int(input("Type another number: "))
#
# result = value_1 + value_2
#
# print(result)

###### Homework #########
value_float_1 = input("Please type a number: ")
value_float_2 = input("Please type another number: ")
value_operator = input("Please choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n your answer:")

if value_operator == '1':
    result = value_float_1 + value_float_2

print(result)
