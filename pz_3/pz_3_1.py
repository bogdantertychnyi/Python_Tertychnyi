# Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у)
# лежит в первой или третьей координатной четверти».

x = input("Введите число X-координаты ")
while type(x) != int: # обработка исключений
  try:
    x = int(x)
  except ValueError:
    print("Неправильно ввели!")
    x = input("Введите число X-координаты ")

y = input("Введите число Y-координаты ")
while type(y) != int: # обработка исключений
  try:
    y = int(y)
  except ValueError:
    print("Неправильно ввели!")
    y = input("Введите число Y-координаты ")

# определение четверти
if x > 0 and y > 0:
    print("Точка с заданными координатами лежит в первой четверти.")
elif x < 0 and y < 0:
    print("Точка с заданными координатами лежит в третьей четверти.")
else:
    print("Точка с заданными координатами не лежит ни в первой, ни в третьей четверти.")
