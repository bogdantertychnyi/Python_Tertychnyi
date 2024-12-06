# Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
# наименьший периметр треугольника, вершины которого принадлежат различным
# точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором
# они перечислены при задании множества A).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат.

import math

def distance(x1, y1, x2, y2):
    # Вычисляем расстояние
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

N = input("Введите количество точек (больше 2):  ")
while type(N) != int:   # обработка исключений
    try:
        N = int(N)
        if N < 3:
            print("Ошибка: количество точек должно быть больше 2.")
            N = input("Введите количество точек (больше 2):  ")
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите количество точек (больше 2):  ")

# Ввод координат точек
x_coords = []
y_coords = []
for i in range(N):
    x_element = input(f'Введите координату x для точки {i + 1}: ')
    while type(x_element) != int:  # обработка исключений
        try:
            x_element = int(x_element)
        except ValueError:
            print("Неправильно ввели!")
            x_element = input(f'Введите координату x для точки {i + 1}: ')
    y_element = input(f'Введите координату y для точки {i + 1}: ')
    while type(y_element) != int:  # обработка исключений
        try:
            y_element = int(y_element)
        except ValueError:
            print("Неправильно ввели!")
            y_element = input(f'Введите координату y для точки {i + 1}: ')
    x_coords.append(x_element)
    y_coords.append(y_element)


perimeters = []

# Перебор комбинаций точек
for i in range(N):
    for j in range(i + 1, N):  # j должен быть больше, чем i
        for k in range(j + 1, N):  # k должен быть больше, чем j
            # Точки треугольника
            point1 = (x_coords[i], y_coords[i])
            point2 = (x_coords[j], y_coords[j])
            point3 = (x_coords[k], y_coords[k])

            side_a = distance(x_coords[i], y_coords[i], x_coords[j], y_coords[j])
            side_b = distance(x_coords[j], y_coords[j], x_coords[k], y_coords[k])
            side_c = distance(x_coords[k], y_coords[k], x_coords[i], y_coords[i])

            # Здесь вы можете делать что-то с полученными точками
            print(f"Точки треугольника: {point1}, {point2}, {point3}")

            # Вычисление периметра
            perimeter = side_a + side_b + side_c
            print("Периметр: ", perimeter)
            perimeters.append(perimeter)

# Нахождение минимального периметра
min_perimeter = min(perimeters)
print(f"Минимальный периметр: {min_perimeter}")