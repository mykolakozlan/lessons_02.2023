# розпаковка tuple та list
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())


############# розпаковка tuple та list
# my_value = (1, 2, "Test", None)

# value_1, value_2 = my_value[:2]   # розпаковка через зріз
# value_1, value_2, _ = my_value   # розпаковка через тимчасову змінну "_"
# value_1, value_2, *tmp = my_value  # множинна розпаковка через тимчасову змінну "_"

# print(my_value)
# print(*my_value)
# print(value_1, value_2, _)


# for _ in range(5):
#     print("Hello")

############ dict()

# val_list = [1, 2, 3]
# Ключ до словника це завжди НЕЗМІННИЙ тип даний(якщо цікаво, почитай про хеш таблиці)
value = {
    "key": "value",
    1: "blabla",
    True: "jjjj",
    (1, 2): True,
    None: True,
    1.2: True,
}

# print(value[(1, 2)])
#
address = {
    "country": "Ukraine",
    "city": "Kyiv",
    "street": "Kyiv",

}

person = {
    "first_name": "Nick",
    "last_name": "Kozlan",
    "email": "mail@gmail.com",
    "password": "1111111",
    "address": address,
}

person_2 = {
    "first_name": "Nick1",
    "last_name": "Kozlan2",
    "email": "mail@gmail.com333",
    "password": "111111122",
    "address": address,
}

our_group = [person, person_2]

# print(our_group)

# print(person['address']['city'])

# print(list(person.keys())) # keys - список ключів до словнику
# print(list(person.values())) # values - значення які лежать в словнику
# print(person.items()) # items - все що лежать в словнику [('last_name', 'Kozlan'), ('email', 'mail@gmail.com')]

# for i in person:    #дивиться в ключі
#     print(i, person[i])
#
# for key, value in person.items():
#     print(key, value)


# if 'first_name' in person:  #дивиться в ключі
#     first_name = person['first_name']
# else:
#     first_name = 0
#
# # first_name = person.get('first_name', False)  #додає можливість видачі дефолтного значення в разі відсутності ключа
# print(first_name)

# person_3 = {}
#
# person_3['first_name'] = "Nikolas"
# person_3['last_name'] = "Nikolas"
# person_3['phone'] = "+380000000"
#
# print(person)
#
# from random import randint
# #
# #
# # number = randint(1, 6)
# #
# # dice_dict = {
# #     1: "This is 1",
# #     2: "This is 2",
# #     3: "This is 3",
# #     4: "This is 4",
# #     5: "This is 5",
# #     6: "This is 6",
# # }
# #
# # print(dice_dict[number])

# val_dict = {
#     1: "This is 1",
#     2: "This is 2",
# }
#
# new_dict = {
#     2: "This is 3",
#     4: "This is 4",
# }
# val_dict.update(new_dict)
# print(val_dict)
#
# val_dict[1] = "This is 33333"
# print(val_dict)
# val_dict[1] = "This is 1111"
# val_dict[4] = "This is 1111"
#
# # print(val_dict)
#
# # ASCII       ord("a") chr(97)
#
# alphabet_dict = {}
# alphabet_value_dict = {}
#
# for index in range(ord("a"), ord("z") + 1):
#     alphabet_dict[index] = chr(index)
#     # alphabet_value_dict[chr(index)] = index
# # print(alphabet_value_dict)
# #
# # for key, value in alphabet_dict.items():
# #     alphabet_value_dict[value] = key
#
# for key in alphabet_dict:  # лише ключі
#     alphabet_value_dict[alphabet_dict[key]] = key
#
# # print(alphabet_value_dict)
#
#
# # val_list = [index for index in range(1, 10)]
#
# # val_dict = {index: index**2 for index in range(1, 10)}
# val_dict = {index: person[index] for index in person}
# print(val_dict)
#
# value_list = [1, 2, 3]
# value_list.pop()
#
# val = val_dict.pop('email')
#
# print(val)


