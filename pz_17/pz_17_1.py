import tkinter as tk

def calculate_sum():
    try:
        # Получаем значение N из поля ввода
        N = int(entry.get())

        # Проверяем, что N больше 0
        if N <= 0:
            result_label.config(text="N должно быть больше 0")
            return

        # Вычисляем сумму
        total = sum(i*i for i in range(N, 2*N + 1))

        # Отображаем результат
        result_label.config(text=f"Сумма равна: {total}")

    except ValueError:
        # Если введено некорректное значение, выводим сообщение об ошибке
        result_label.config(text="Пожалуйста, введите корректное целое число")

# Создаем основное окно
root = tk.Tk()
root.title("Сумма квадратов")

# Метка и поле ввода для N
label = tk.Label(root, text="Введите значение N:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка для вычисления суммы
calculate_button = tk.Button(root, text="Вычислить сумму", command=calculate_sum)
calculate_button.pack(pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Запускаем основной цикл приложения
root.mainloop()
