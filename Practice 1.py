import random

lower_bound = int(input("Введите нижнюю границу: "))
upper_bound = int(input("Введите верхнюю границу: "))
num_of_elements = int(input("Введите количество чисел: "))
if num_of_elements < 2:
    print("Недостаточно элементов для сортировки.")
else:
    random_numbers = [
        random.randint(lower_bound, upper_bound) for _ in range(num_of_elements)
    ]

    print("Исходный список:", random_numbers)

    sorted_numbers_ascending = sorted(random_numbers)
    print("Список по возрастанию:", sorted_numbers_ascending)

    sorted_numbers_descending = sorted(random_numbers, reverse=True)
    print("Список по убыванию:", sorted_numbers_descending)
