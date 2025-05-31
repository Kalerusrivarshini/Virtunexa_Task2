import tkinter as tk
from tkinter import messagebox
from calculator import add, subtract, multiply, divide

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operation = operator.get()

        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            result = "Invalid"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Calculator - GUI")

tk.Label(root, text="First Number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Operation").grid(row=2, column=0)
operator = tk.StringVar(root)
operator.set("+")
tk.OptionMenu(root, operator, "+", "-", "*", "/").grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
