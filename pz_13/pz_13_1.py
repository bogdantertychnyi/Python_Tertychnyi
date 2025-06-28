# В двумерном списке элементы последней строки заменить на 0.

import random

a = int(input('Введите количество столбцов: '))
n = int(input('Введите количество строк: '))

matrix = [list(random.randint(-15, 15) for _ in range(a)) for _ in range(n)]
print("Исходная матрица:")
list(map(print, matrix))

updated_matrix = list(map(lambda i: list(map(lambda _: 0, matrix[i])) if i == n - 1 else matrix[i], range(n)))

print("Матрица после замены элементов последней строки на 0:")
list(map(print, updated_matrix))
