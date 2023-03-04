# list comprehension
# sets
# sets methods(union(), difference(), intersection())

# val_string = "123456"
#
# # val_list = []
# # print(id(val_list))
# # for symbol in val_string:
# #     if not (int(symbol)**2) % 2:
# #         val_list.append(    int(symbol)**2      )
#
# # val_list = [symbol for symbol in val_string]
# # val_list = [int(symbol)**2 for symbol in val_string]
# val_list = [int(symbol)**2 for symbol in val_string if (int(symbol)**2) % 2 == 0]
# print(id(val_list))
# print(val_list)

# Command + Option + L(Mac) / Ctrl + Alt + L (Win) вирівнювання по PEP8

################ Set ##########

# value_list = ["d", "h", "d", "r"]
# value_list = [1, 23, 4, 5, 6]
# print(value_list)
# value_set = set(value_list)
# print(value_set)
# value_set = set()

# val_set_1 = {1, 2, 3}
# val_set_2 = {11, 2, 31, 3}

# result = val_set_1.union(val_set_2) # плюсує всі уікальні
# print(result)

# result = val_set_2.difference(val_set_1) # мінусує всі уікальні ПОРЯДОК ВАЖЛИВИЙ
# print(result)

# result = val_set_1.intersection(val_set_2) # виводить лише спільні значення
# print(result)



# (union(), difference(), intersection()
