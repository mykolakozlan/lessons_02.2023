# homework review
# debuger
# for (range, enumerate)
# str methods(isalpha, rfind, replace, startwith)


##### Homework sample ###########

# print("Welcome to calculator.")

# result = 0
# operator = ""
#
# try:
#     first = float(input("Enter first number: "))
#     second = float(input("Enter second number: "))
#     act = input("Please choose an operation. \n1 - '+'\n2 - '-'\n3 - '*'\n4 - '/': ")
#
#     if act == '1':
#         result = first + second
#         operator = '+'
#     elif act == '2':
#         result = first - second
#         operator = '-'
#     elif act == '3':
#         result = first * second
#         operator = '*'
#     elif act == '4':
#         result = first / second
#         operator = '/'
#     else:
#         print("Incorrect choice of operation")
#     answer = f"{first} {operator} {second} = {result}"
#
# except ValueError:
#     print("ValueError")
# except ZeroDivisionError:
#     print("ZeroDivisionError")

#### For loop ########


# for letter in value:
#     print(letter)

# range(10) - до десяти(виключно)(0-9)
# range(5, 10) - від 5 до десяти(виключно)(5-9)
# range(5, 10, 2) - від 5 до десяти(виключно), остання цифра це крок (5,7,9)

# for index in range(10):
#     print(index)


# for index in range(len(value)):
#     print(index, )


# value = "hello"
#
# for letter in value:
#     if letter:
#         print()
#     else:
#         pass

# for index in range(len(value)):
#   print(value[index], index)
# #
# for letter in value:
#     print(letter, value.index(letter))
#
# print("!!!!!!")

# enumerate() перебирає змінну і видає і індекс і символ
#
# for index, letter in enumerate(value):
#     print(letter, index)
#
# value = "hello123456".index()
# value_1 = "hello12345jjj6".index()
# value_2 = "hello12345699".index()


# value = "YYYYYHe,,,llo!!!123456"

# for letter in value:
#     # print(letter.isalpha())
#     if letter.upper() in "EYUIOAJ":
#         print(letter)

# value = "img_123.png"
# print(value)
# value = value.replace('.png', '.jpg')
# print(value)

# print(value.startswith("img"))

act = "+"

if act != '+' and act != '-' and act != '*' and act != '/':
    print('Введи тільки пропоновану дію')
else:
    print("win")
