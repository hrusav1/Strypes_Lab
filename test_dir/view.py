# view.py

import tkinter as tk
from tkinter import ttk, messagebox

class CollectionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Collection Manager")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def add_tab(self, tab_class, title, controller):
        tab = tab_class(self.notebook, controller)
        self.notebook.add(tab.frame, text=title)

class BaseTab:
    def __init__(self, parent, controller, tab_title):
        self.parent = parent
        self.controller = controller

        self.frame = ttk.Frame(self.parent)  # Use parent directly as it's already a Notebook
        self.parent.add(self.frame, text=tab_title)

        self.setup_ui()

    def setup_ui(self):
        # Left side - Listbox with scrollbar
        self.list_frame = ttk.Frame(self.frame)
        self.list_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.items_listbox = tk.Listbox(self.list_frame, width=30, yscrollcommand=self.scrollbar.set)
        self.items_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.items_listbox.yview)

        self.items_listbox.bind("<<ListboxSelect>>", self.on_select_item)

        # Right side - Details display with scrollable frame
        self.details_frame = ttk.Frame(self.frame)
        self.details_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.inner_frame = ttk.Frame(self.details_frame)
        self.inner_frame.pack(fill=tk.BOTH, expand=True)

    def on_select_item(self, event):
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            item = self.get_selected_item(index)
            self.display_item_details(item)

    def get_selected_item(self, index):
        raise NotImplementedError("Subclasses should implement get_selected_item method")

    def display_item_details(self, item):
        # Clear previous details
        for widget in self.inner_frame.winfo_children():
            widget.pack_forget()

        # Display item details
        row = 0
        for key, value in item.items():
            label = ttk.Label(self.inner_frame, text=f"{key.capitalize()}:")
            label.pack(padx=5, pady=5, anchor="w")

            entry = ttk.Entry(self.inner_frame)
            entry.insert(0, value)
            entry.pack(fill=tk.X, padx=5, pady=5)

            row += 1

        # Save button at the bottom
        save_button = ttk.Button(self.inner_frame, text="Save", command=self.save_item)
        save_button.pack(pady=10)

    def save_item(self):
        raise NotImplementedError("Subclasses should implement save_item method")

    def update_items_listbox(self, items):
        self.items_listbox.delete(0, tk.END)
        for item in items:
            self.items_listbox.insert(tk.END, self.get_listbox_display_text(item))

    def get_listbox_display_text(self, item):
        raise NotImplementedError("Subclasses should implement get_listbox_display_text method")

class TabMovies(BaseTab):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Movies")

    def get_selected_item(self, index):
        return self.controller.model.get_items("movies")[index]

    def save_item(self):
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            item = self.get_selected_item(index)
            self.controller.movies_controller.save_item(item, self.inner_frame)
        else:
            messagebox.showwarning("Warning", "Select a movie to save.")

    def get_listbox_display_text(self, item):
        return item.get('title', 'Unknown')

class TabGames(BaseTab):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Games")

    def get_selected_item(self, index):
        return self.controller.model.get_items("games")[index]

    def save_item(self):
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            item = self.get_selected_item(index)
            self.controller.games_controller.save_item(item, self.inner_frame)
        else:
            messagebox.showwarning("Warning", "Select a game to save.")

    def get_listbox_display_text(self, item):
        return item.get('Title', 'Unknown')

class TabBooks(BaseTab):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Books")

    def get_selected_item(self, index):
        return self.controller.model.get_items("books")[index]

    def save_item(self):
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            item = self.get_selected_item(index)
            self.controller.books_controller.save_item(item, self.inner_frame)
        else:
            messagebox.showwarning("Warning", "Select a book to save.")

    def get_listbox_display_text(self, item):
        return item.get('title', 'Unknown')
