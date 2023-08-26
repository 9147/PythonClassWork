import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(entry_n1.get()) + float(entry_n2.get()))
    except ValueError():
        messagebox.showerror("Error", "Print valid numbers")

def subtract():
    try:
        result.set(float(entry_n1.get()) - float(entry_n2.get()))
    except ValueError():
        messagebox.showerror("Error", "Print valid numbers")

def multiply():
    try:
        result.set(float(entry_n1.get()) * float(entry_n2.get()))
    except ValueError():
        messagebox.showerror("Error", "Print valid numbers")

def divide():
    try:
        n2 = float(entry_n2.get())
        if n2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
        else:
            result.set(float(entry_n1.get()) / n2)

    except ValueError():
        messagebox.showerror("Error", "Print valid numbers")

window =tk.Tk()
window.title("Calculator")
entry_n1 = tk.Entry(window)
entry_n1.pack()
entry_n2 = tk.Entry(window)
entry_n2.pack()
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()
add_button = tk.Button(window, text="ADD", command=add)
add_button.pack()
subtract_button = tk.Button(window, text="SUBTRACT", command=subtract)
subtract_button.pack()
multiply_button = tk.Button(window, text="MULTIPLY", command=multiply)
multiply_button.pack()
divide_button = tk.Button(window, text="DIVIDE", command=divide)
divide_button.pack()
window.mainloop()