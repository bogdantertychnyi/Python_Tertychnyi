import tkinter as tk

def calc():
    try:
        N = int(entry.get())
        total = sum(i*i for i in range(N, 2*N + 1))

        result_label.config(text=f"Сумма равна: {total}")

    except ValueError:
        result_label.config(text="Пожалуйста, введите корректное целое число")

root = tk.Tk()
root.title("Сумма квадратов")

label = tk.Label(root, text="Введите значение N:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

calculate_button = tk.Button(root, text="Вычислить сумму", command=calc)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
