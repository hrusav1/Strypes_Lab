import tkinter as tk
from tkinter import messagebox
from math import sqrt, factorial

class CalculatorModel:
    def __init__(self):
        self.memory = []
        self.current_value = ""

    def clear_memory(self):
        self.memory = []

    def recall_memory(self):
        return self.format_result(sum(self.memory)) if self.memory else "0"

    def clear_entry(self):
        self.current_value = ""

    def all_clear(self):
        self.clear_memory()
        self.clear_entry()

    def change_sign(self, value):
        return str(-float(value)) if value else ""

    def calculate(self, expression):
        operators = ['+', '-', '*', '/']
        for operator in operators:
            if operator in expression:
                try:
                    left, right = expression.split(operator)
                    left = float(left)
                    right = float(right)
                    if operator == '+':
                        return self.format_result(left + right)
                    elif operator == '-':
                        return self.format_result(left - right)
                    elif operator == '*':
                        return self.format_result(left * right)
                    elif operator == '/':
                        if right != 0:
                            return self.format_result(left / right)
                        else:
                            return "inf"  # Handle division by zero
                except ValueError:
                    raise ValueError("Invalid input")
        raise ValueError("Invalid input")

    def square_root(self, value):
        try:
            return self.format_result(sqrt(float(value)))
        except ValueError:
            raise ValueError("Invalid input")

    def calculate_factorial(self, value):
        try:
            return self.format_result(factorial(int(value)))
        except ValueError:
            raise ValueError("Invalid input")

    def add_to_memory(self, value):
        self.memory.append(float(value))

    def subtract_from_memory(self, value):
        self.memory.append(-float(value))

    def format_result(self, result):
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return str(result) if isinstance(result, int) else f"{result:.5g}"

# Initialize main window
root = tk.Tk()
root.title("Calculator")

# Create calculator model
calculator = CalculatorModel()

# Display
tk.Label(root, text="Display", font=("Arial", 14)).grid(row=0, column=0, columnspan=6)
display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=28, borderwidth=4, justify='right')
display.grid(row=1, column=0, columnspan=6)

# Memory display
tk.Label(root, text="Memory", font=("Arial", 14)).grid(row=3, column=6)
memory_display = tk.Listbox(root, font=("Arial", 12), height=10, width=20, bd=5)
memory_display.grid(row=1, column=6, rowspan=10)

# Prevent pasting into the display
def disable_paste(event):
    return "break"

display.bind("<Control-v>", disable_paste)
display.bind("<Control-V>", disable_paste)

# Functions
def btn_click(item):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(item))

def clear_entry():
    calculator.clear_entry()
    display.delete(0, tk.END)

def all_clear():
    calculator.all_clear()
    display.delete(0, tk.END)
    update_memory_display()

def calculate():
    try:
        result = calculator.calculate(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
        return result
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return None

def memory_clear():
    calculator.clear_memory()
    update_memory_display()

def memory_plus():
    if display.get():
        result = calculate()  # Perform the calculation
        if result is not None:
            calculator.add_to_memory(result)
            update_memory_display()
    else:
        messagebox.showinfo("Usage Error", "Use the m+ button after performing a calculation. For example:\n1. Enter '5*5'\n2. Press '='\n3. Press 'm+' to store 25 in memory.")

def memory_minus():
    if display.get():
        result = calculate()  # Perform the calculation
        if result is not None:
            calculator.subtract_from_memory(result)
            update_memory_display()
    else:
        messagebox.showinfo("Usage Error", "Use the m- button after performing a calculation. For example:\n1. Enter '5*5'\n2. Press '='\n3. Press 'm+' to store 25 in memory.\n4. Enter '5+5'\n5. Press '='\n6. Press 'm-' to subtract 10 from memory.")

def memory_recall():
    display.delete(0, tk.END)
    display.insert(0, calculator.recall_memory())

def update_memory_display():
    memory_display.delete(0, tk.END)
    for i, mem in enumerate(calculator.memory):
        memory_display.insert(tk.END, f"{i+1}: {calculator.format_result(mem)}")

def change_sign():
    try:
        value = display.get()
        result = calculator.change_sign(value)
        display.delete(0, tk.END)
        display.insert(0, result)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def square_root():
    try:
        value = display.get()
        if value:
            result = calculator.square_root(value)
            display.delete(0, tk.END)
            display.insert(0, result)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def calculate_factorial():
    try:
        value = display.get()
        if value:
            result = calculator.calculate_factorial(value)
            display.delete(0, tk.END)
            display.insert(0, result)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

buttons = []
for text in button_texts:
    if text == "=":
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, bd=8, font=("Arial", 18), command=lambda t=text: btn_click(t))
    buttons.append(button)

# Memory buttons
memory_buttons = [
    ("mc", memory_clear),
    ("m+", memory_plus),
    ("m-", memory_minus),
    ("mr", memory_recall),
    ("CE", clear_entry),
    ("AC", all_clear),
    ("+/-", change_sign),
    ("√", square_root),
    ("!", calculate_factorial)
]

for i, (text, command) in enumerate(memory_buttons):
    button = tk.Button(root, text=text, padx=20, pady=20, bd=8, font=("Arial", 18), command=command)
    buttons.append(button)

# Layout
for i in range(4):
    for j in range(4):
        buttons[i * 4 + j].grid(row=i + 2, column=j)

for i in range(len(memory_buttons)):
    buttons[16 + i].grid(row=6 + i // 3, column=i % 3, columnspan=1)

if __name__ == "__main__":
    # Run the application
    root.mainloop()