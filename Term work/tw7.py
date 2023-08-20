'''
Develop the following GUI application.
'''

import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(entry_num1.get()) + float(entry_num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def subtract():
    try:
        result.set(float(entry_num1.get()) - float(entry_num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def multiply():
    try:
        result.set(float(entry_num1.get()) * float(entry_num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def divide():
    try:
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result.set(float(entry_num1.get()) / num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry fields for numbers
entry_num1 = tk.Entry(window)
entry_num1.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

# Result display
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()

# Buttons for operations
add_button = tk.Button(window, text="Add", command=add)
add_button.pack()

subtract_button = tk.Button(window, text="Subtract", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(window, text="Multiply", command=multiply)
multiply_button.pack()

divide_button = tk.Button(window, text="Divide", command=divide)
divide_button.pack()

# Start the GUI event loop
window.mainloop()
