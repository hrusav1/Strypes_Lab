import tkinter as tk
from tkinter import ttk

class BMIModel:
    def __init__(self):
        self.height = None
        self.weight = None
        self.bmi = None

    def calculate_bmi(self, height, weight):
        try:
            self.height = float(height)
            self.weight = float(weight)
            self.bmi = self.weight / (self.height ** 2)
            return self.bmi, self.get_bmi_category()
        except ValueError:
            return None, "Invalid Data"

    def get_bmi_category(self):
        if self.bmi < 18.5:
            return "Underweight", "blue"
        elif 18.5 <= self.bmi <= 24.9:
            return "Normal Weight", "green"
        elif 25 <= self.bmi <= 29.9:
            return "Overweight", "yellow"
        else:
            return "Obese", "red"

class BMIView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("BMI Calculator")

        # Set minimum size of the window
        self.root.minsize(300, 200)

        # Frame for organizing widgets
        input_frame = ttk.Frame(self.root, padding="20")
        input_frame.pack(padx=20, pady=20, expand=True, fill='both')

        # Height Input
        height_label = ttk.Label(input_frame, text="Height (m):")
        height_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.height_entry = ttk.Entry(input_frame, width=10)
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)

        # Weight Input
        weight_label = ttk.Label(input_frame, text="Weight (kg):")
        weight_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.weight_entry = ttk.Entry(input_frame, width=10)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        # Calculate Button
        calculate_button = ttk.Button(input_frame, text="Calculate", command=self.controller.calculate_bmi)
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

        # BMI Result Label
        self.bmi_label = ttk.Label(input_frame, text="")
        self.bmi_label.grid(row=3, column=0, columnspan=2, pady=10)

        # BMI Category Label
        self.bmi_category_label = ttk.Label(input_frame, text="")
        self.bmi_category_label.grid(row=4, column=0, columnspan=2)

    def get_height(self):
        return self.height_entry.get()

    def get_weight(self):
        return self.weight_entry.get()

    def display_bmi(self, bmi, category, color):
        if bmi is None:
            self.bmi_label.config(text=category)
            self.bmi_category_label.config(text="", foreground="black")
        else:
            self.bmi_label.config(text=f"BMI: {bmi:.2f}")
            self.bmi_category_label.config(text=category, foreground=color)

class BMIController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate_bmi(self):
        height = self.view.get_height()
        weight = self.view.get_weight()
        bmi, category = self.model.calculate_bmi(height, weight)
        if bmi is not None:
            category, color = category
        else:
            color = "black"
        self.view.display_bmi(bmi, category, color)

if __name__ == "__main__":
    root = tk.Tk()
    model = BMIModel()
    controller = BMIController(model, None)  # Temporarily set view to None
    view = BMIView(root, controller)
    controller.view = view  # Now assign the view to the controller
    root.mainloop()

