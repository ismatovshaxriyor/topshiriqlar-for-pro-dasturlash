""" *** ------------ List comprehesion, map, reduce, lambda, filter ------------- *** """

# <=== *** List comprehesion *** ===>

# # <== 1 - masala ==>
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# toq_sonlar = []
# for i in list1:
#     if i % 2 == 1:
#         toq_sonlar.append(i)

# print(f"before List comprehesion: {toq_sonlar}")

# toq_sonlar = [i for i in list1 if i % 2 == 1]
# print(f"after List comprehesion: {toq_sonlar}")


# # <== 2 - masala ==>
# reyses = [
#     ['Toshkent', 'Buxoro'],
#     ['Farg\'ona', 'Jizzax'],
#     ['Jizzax', 'Navoiy'],
#     ['Andijon', 'Farg\'ona'],
#     ['Samarqand', 'Andijon'],
#     ['Buxoro', 'Samarqand']
# ]

# from_city = [i[0] for i in reyses]
# print(f"Samalayotlar havoga ko'tariladigan shaharlar: {from_city}")


# # <== 3 - masala ==>
# list2 = [1, 2, 3, 'Alice', 'Alice']

# item_index = [i for i in range(len(list2)) if list2[i] == "Alice"]
# print(item_index)


# # <== 4 - masala ==>
# people = [
#     ("John", 240_000),
#     ("Alice", 120_000),
#     ("Ann", 1_100_000),
#     ("Zach", 44_000),
#     ("Sara", 2_000_000)
# ]

# def find_milloners(people):
#     millioners = [name for name, money in people.items() if money > 1_000_000]
#     return millioners

# people_data_1 = {
#     'Alice': 1_100_000,
#     'Bob': 998_170,
#     'Carol': 1_229_080,
#     'Frank': 881_230,
#     'Eve': 93_121
# }

# people_data_2 = {
#     'Alice': 1_100_000,
#     'Bob': 998_170,
#     'Frank': 1_881_230,
#     'Eve': 321_121
# }

# def test():
#     assert find_milloners(people_data_1) == ['Alice', 'Carol']
#     assert find_milloners(people_data_2) == ['Alice', 'Frank']

# test()


# # <== 5 - masala ==>
# a = [[i, j] for i in range(3) for j in range(3)]
# print(a)


# # <== 6 - masala ==>
# txt = """
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
# """

# list_txt = txt.split()

# lenght_5 = [i for i in list_txt if len(i) == 4]
# print(lenght_5)


# ------------------------------------------------------
# <=== *** ZIPlash *** ===>

# list1 = ['ism', 'familya', 'yosh']
# list2 = ['shaxriyor', 'ismatov', 17]

# zip_lists = list(zip(list1, list2))
# print(zip_lists)


# # <=== *** UNZIPlash *** ===>
# list1_new, list2_new = zip(*zip_lists)
# print(list1_new)
# print(list2_new)
# -------------------------------------------------------


# # <== 7 - masala ==>
# ustun_nomlari = ['name', 'salary', 'job']
# qatorlar = [
#     ('Alice', 180_000, 'data scientist'),
#     ('Bob', 99_000, 'project manager'),
#     ('Frank', 87_000, 'backend developer')
# ]

# db = [dict(zip(ustun_nomlari, qator)) for qator in qatorlar]
# print(db)


# -------------------------------------------------------
# <=== *** Lambda *** ===>

# # <== 8 - masala ==>
# summa = lambda a, b, c: a + b + c

# print(summa(1, 2, 3))

# -------------------------------------------------------

# <=== *** Map *** ===>

# <== 9 - masala ==>
# str_numbers = ['1', '2', '3', '4', '2', '1', '3', '1']
# int_numbers = map(int, str_numbers)

# print(list(int_numbers))


# # <== 10 - masala ==>
# numbers = [2, 1, 6, 4, 1, 5, 7, 2, 3]
# numbers_kv = map(lambda x: x**2, numbers)

# print(list(numbers_kv))


# # <== 11 - masala ==>
# numbers1, numbers2 = [4, 2, 7, 2], [8, 4, 6, 2]
# x = list(map(lambda x, y: x - y, numbers1, numbers2))

# print(x)


# # <== 12 - masala ==>
# txt = "dummy text of the printing and typesetting industry".split()
# toUpper = list(map(str.upper, txt))

# print(toUpper)


# -------------------------------------------------------

# # <=== *** Reduce *** ===>

# <== 13 - masala ==>
# from functools import reduce

# n = 5
# factorial = reduce(lambda x, y: x * y, range(1, n + 1))

# print(factorial)


# -------------------------------------------------------

# <=== *** Filter *** ===>

# # <== 14 - masala ==>
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = filter(lambda x: x % 2 != 0, numbers)

# print(list(x))