#В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
#раза.

import random

a = int(input('Введите количество столбцов: '))
n = int(input('Введите количество строк: '))

matrix = list(([random.randint(1, 15) for _ in range(a)] for _ in range(n)))
print("Исходная матрица:")
list(map(print, matrix))

N = int(input(f'Введите номер столбца (0 до {a-1}): '))

updated_matrix = list(map(lambda row: list(map(lambda i: row[i] * 2 if i == N else row[i], range(a))), matrix))

print("Обновленная матрица:")
list(map(print, updated_matrix))
