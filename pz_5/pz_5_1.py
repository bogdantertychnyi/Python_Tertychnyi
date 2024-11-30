# Составить функцию решения задачи: из заданного числа вычли сумму его цифр.Из
# результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
# получится нуль?

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10  # добавляем последнюю цифру
        num //= 10  # удаляем последнюю цифру
    return total

def steps_until_zero(num):
    t = 0  # счетчик
    while num != 0:
        d = sum_of_digits(num)  # сумма цифр числа
        num = num - d
        t += 1
    return t

# Ввод числа
num = input("Введите целое число: ")
while True:  # обработка исключений
    try:
        num = int(num)
        if num > 0:  # Проверка на положительность
            break
        else:
            num = abs(num)
    except ValueError:
        print("Неправильно ввели! Попробуйте снова.")
        num = input("Введите целое число: ")

# Вывод результата
print(steps_until_zero(num))