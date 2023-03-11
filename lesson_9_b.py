# import string
# from string import (ascii_uppercase, ascii_lowercase, ascii_letters
# from string import ascii_uppercase as alphabet_upper
# from string import ascii_lowercase as alphabet_lower
# from string import *

# moduls
# def


# alphabet_upper = ascii_uppercase
# ascii_letters = ascii_lowercase
#
# print(alphabet_upper)
# print(ascii_letters)


# def my_fn(a, b):
#
#     c = a + b
#
#     return c

import random

triangle = []


#
# dot_1 = {
#     "x": random.randint(1, 100),
#     "y": random.randint(1, 100),
#     "z": random.randint(1, 100)
# }
#
# dot_2 = {
#     "x": random.randint(1, 100),
#     "y": random.randint(1, 100),
#     "z": random.randint(1, 100)
# }
#
# dot_3 = {
#     "x": random.randint(1, 100),
#     "y": random.randint(1, 100),
#     "z": random.randint(1, 100)
# }

# ctrl + shift + F(Win)  command + shift + F(mac) пошук по всьому проекту


def creating_dots(x_coord, y_coord, z_coord):
    dot = {
        "x": x_coord,
        "y": y_coord,
        "z": z_coord,
    }

    return dot


triangle = [
    creating_dots(
        random.randint(1, 50),
        random.randint(1, 50),
        random.randint(1, 50),
    ),
    creating_dots(random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)),
    creating_dots(random.randint(1, 50), random.randint(1, 50), random.randint(1, 50))
]

square = [
    creating_dots(random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), ),
    creating_dots(random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)),
    creating_dots(random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)),
    creating_dots(random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)),
]


def printing_obj(obj_coord, obj_type):
    print(f"This is a {obj_type}, it's' coordinates are:{obj_coord}")

    return None




# printing_obj(triangle, "triangle")


value = printing_obj(triangle, "triangle")
print(value)
# print(triangle)
# print(square)


# dot = {
#     "x": random.randint(1, 60),
#     "y": random.randint(1, 60),
#     "z": random.randint(1, 60),
# }
#
# dot_1 = {
#     "x": random.randint(1, 60),
#     "y": random.randint(1, 60),
#     "z": random.randint(1, 60),
# }
#
# for key_1, val_1 in dot.items():
#
#     for key_2, val_2 in dot_1.items():
#         pass




