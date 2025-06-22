import tkinter as tk
from tkinter import messagebox
import logging

# Set up logging
logging.basicConfig(filename='calc_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        else:
            result = "Invalid operation"

        # Show result
        result_label.config(text=f"Result: {result}")

        # Log the result
        logging.info(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# GUI setup
root = tk.Tk()
root.title("Calculator with Logging")
root.geometry("400x300")

tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Select Operation:").pack(pady=5)
operator = tk.StringVar(root)
operator.set("Add")
tk.OptionMenu(root, operator, "Add", "Subtract", "Multiply", "Divide").pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

root.mainloop()
