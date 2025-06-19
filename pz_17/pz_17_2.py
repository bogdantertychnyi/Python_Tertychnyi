import tkinter as tk
from tkinter import ttk

def create_signup_form():
    root = tk.Tk()
    root.title("Sign Up")
    root.geometry("400x600")
    root.configure(bg="#000121")  # Обновленный цвет фона

    top_frame = tk.Frame(root, bg="orange")
    top_frame.pack(fill=tk.X)
    header = tk.Label(top_frame, text="Sign Up", bg="orange", fg="white", font=("Arial", 16))
    header.pack(side=tk.LEFT, padx=10)

    form_frame = tk.Frame(root, bg="#000121")
    form_frame.pack(pady=20)

    fields = [
        "First Name", "Last Name", "Screen Name",
        "Date of Birth", "Gender", "Country",
        "E-mail", "Phone", "Password", "Confirm Password"
    ]

    entries = []
    for i, field in enumerate(fields):
        label = tk.Label(form_frame, text=field, bg="#000121", fg="yellow")
        label.grid(row=i, column=0, sticky=tk.W, pady=5)

        if field == "Date of Birth":
            month_var = tk.StringVar()
            month_dropdown = ttk.Combobox(form_frame, textvariable=month_var, width=5)
            month_dropdown['values'] = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
            month_dropdown.grid(row=i, column=1, sticky=tk.W, pady=5)

            day_entry = tk.Entry(form_frame, width=5)
            day_entry.grid(row=i, column=2, sticky=tk.W, pady=5)

            year_entry = tk.Entry(form_frame, width=10)
            year_entry.grid(row=i, column=3, sticky=tk.W, pady=5)

        elif field == "Gender":
            gender_var = tk.StringVar(value="")
            male_rb = tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", bg="#000121", fg="white")
            male_rb.grid(row=i, column=1, sticky=tk.W, pady=5)
            female_rb = tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", bg="#000121", fg="white")
            female_rb.grid(row=i, column=2, sticky=tk.W, pady=5)

        elif field == "Country":
            country_var = tk.StringVar()
            country_dropdown = ttk.Combobox(form_frame, textvariable=country_var)
            country_dropdown['values'] = ('USA', 'Canada', 'UK', 'Australia')
            country_dropdown.grid(row=i, column=1, sticky=tk.W, pady=5, columnspan=3)

        else:
            entry = tk.Entry(form_frame)
            entry.grid(row=i, column=1, sticky=tk.W, pady=5, columnspan=3)
            entries.append(entry)

    terms_var = tk.IntVar()
    terms_check = tk.Checkbutton(form_frame, text="I agree to the Terms of Use", variable=terms_var, bg="#000121", fg="white")
    terms_check.grid(row=len(fields), column=0, columnspan=4, pady=10)

    bottom_frame = tk.Frame(root, bg="orange")
    bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)

    submit_button = tk.Button(bottom_frame, text="Submit", bg="green", fg="white")
    submit_button.pack(side=tk.LEFT, padx=10)

    cancel_button = tk.Button(bottom_frame, text="Cancel", bg="red", fg="white")
    cancel_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

create_signup_form()
