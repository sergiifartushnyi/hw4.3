import random

length = random.randint(3, 10)

original_list = [random.randint(0, 100) for _ in range(length)]

print("Список рандомних чисел:", original_list)

first_index =0

third_index = 2

second_last_index = -2

new_list = [original_list[first_index], original_list[third_index], original_list[second_last_index]]

print("Новий список:", new_list)