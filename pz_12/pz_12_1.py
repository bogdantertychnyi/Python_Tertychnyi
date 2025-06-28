# Организовать и вывести последовательность из 20 целых чисел, выбрать не
# повторяющиеся элементы, найти их количество. Элементы больше 5 увеличить в два раза.

import random

numbers = [random.randint(1, 10) for i in range(20)]
unique = set(numbers)
unique2 = list(map(lambda x: x * 2 if x > 5 else x, unique))
count = len(unique)

print("Исходные числа:", numbers)
print("Уникальные числа:", unique)
print("Количество уникальных чисел:", count)
print("Уникальные числа, увеличенные вдвое:", unique2)
