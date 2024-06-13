import tkinter as tk
from tkinter import ttk

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        bmi_label.config(text=f"BMI: {bmi:.2f}")

        if bmi < 18.5:
            bmi_category_label.config(text="Underweight", foreground="blue")
        elif 18.5 <= bmi <= 24.9:
            bmi_category_label.config(text="Normal Weight", foreground="green")
        elif 25 <= bmi <= 29.9:
            bmi_category_label.config(text="Overweight", foreground="yellow")
        else:
            bmi_category_label.config(text="Obese", foreground="red")

    except ValueError:
        bmi_label.config(text="Invalid Data")
        bmi_category_label.config(text="", foreground="black")

root = tk.Tk()
root.title("BMI Calculator")

# Set minimum size of the window
root.minsize(300, 200)

# Frame for organizing widgets
input_frame = ttk.Frame(root, padding="20")
input_frame.pack(padx=20, pady=20, expand=True, fill='both')

# Height Input
height_label = ttk.Label(input_frame, text="Height (m):")
height_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
height_entry = ttk.Entry(input_frame, width=10)
height_entry.grid(row=0, column=1, padx=10, pady=10)

# Weight Input
weight_label = ttk.Label(input_frame, text="Weight (kg):")
weight_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
weight_entry = ttk.Entry(input_frame, width=10)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate Button
calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# BMI Result Label
bmi_label = ttk.Label(input_frame, text="")
bmi_label.grid(row=3, column=0, columnspan=2, pady=10)

# BMI Category Label
bmi_category_label = ttk.Label(input_frame, text="")
bmi_category_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

