import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

class CollectionManager:
    def __init__(self, filename):
        self.filename = filename
        self.collections = {"movies": [], "games": [], "books": []}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.collections = json.load(file)

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.collections, file, indent=4)

    def add_item(self, category, item):
        self.collections[category].append(item)
        self.save_data()

    def update_item(self, category, index, new_item):
        self.collections[category][index] = new_item
        self.save_data()

    def delete_item(self, category, index):
        del self.collections[category][index]
        self.save_data()

    def search_items(self, category, query):
        return [item for item in self.collections[category] if query.lower() in json.dumps(item).lower()]

    def get_items(self, category):
        return sorted(self.collections[category], key=lambda x: x.get('title', x.get('Title', x.get('name', ''))))

class CollectionApp:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager

        self.root.title("Collection Manager")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.tabs = {}
        self.setup_tabs()

    def setup_tabs(self):
        categories = ["movies", "games", "books"]
        for category in categories:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=category.capitalize())
            self.tabs[category] = frame

            self.setup_ui(frame, category)

            # Automatically display items on tab switch
            self.update_items_listbox(category)

    def setup_ui(self, frame, category):
        # Left side - Listbox with scrollbar
        list_frame = ttk.Frame(frame)
        list_frame.pack(side=tk.LEFT, fill=tk.Y)

        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.items_listbox = tk.Listbox(list_frame, width=30, yscrollcommand=scrollbar.set)
        self.items_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.items_listbox.yview)

        self.items_listbox.bind("<<ListboxSelect>>", lambda event: self.on_select_item(category))

        # Right side - Details display with scrollable frame
        details_frame = ttk.Frame(frame)
        details_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar for details frame
        details_scrollbar = tk.Scrollbar(details_frame)
        details_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Canvas to hold the scrollable frame
        canvas = tk.Canvas(details_frame, yscrollcommand=details_scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        details_scrollbar.config(command=canvas.yview)

        # Scrollable frame inside canvas
        self.inner_frame = ttk.Frame(canvas)
        self.inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Details labels and entries
        self.labels = {}
        self.entries = {}

        # Add new button, delete button, and search
        button_frame = ttk.Frame(frame)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(button_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5)
        search_button = ttk.Button(button_frame, text="Search", command=lambda: self.search_items(category))
        search_button.pack(side=tk.LEFT, padx=5)

        add_new_button = ttk.Button(button_frame, text=f"Add New {category.capitalize()}",
                                    command=lambda: self.add_new_item(category))
        add_new_button.pack(side=tk.LEFT, padx=5)

        delete_button = ttk.Button(button_frame, text=f"Delete {category.capitalize()}",
                                   command=lambda: self.delete_item(category))
        delete_button.pack(side=tk.LEFT, padx=5)

    def update_items_listbox(self, category):
        items = self.manager.get_items(category)
        self.items_listbox.delete(0, tk.END)
        for item in items:
            if category == "movies":
                self.items_listbox.insert(tk.END, item.get('Title', "Unknown"))
            elif category == "games":
                self.items_listbox.insert(tk.END, item.get('Title', "Unknown"))  # Use 'Title' for games
            elif category == "books":
                self.items_listbox.insert(tk.END, item.get('Title', "Unknown"))  # Use 'Title' for books
            else:
                self.items_listbox.insert(tk.END, "Unknown")

    def on_select_item(self, category):
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            item = self.manager.get_items(category)[index]
            self.display_item_details(category, item)

    def display_item_details(self, category, item):
        # Clear previous details
        for widget in self.inner_frame.winfo_children():
            widget.pack_forget()

        # Display item details
        self.labels = {}
        self.entries = {}

        row = 0
        for key, value in item.items():
            label = ttk.Label(self.inner_frame, text=f"{key.capitalize()}:")
            label.pack(padx=5, pady=5, anchor="w")
            self.labels[key] = label

            entry = ttk.Entry(self.inner_frame)
            entry.insert(0, value)
            entry.pack(fill=tk.X, padx=5, pady=5)
            self.entries[key] = entry

            row += 1

        # Save button at the bottom
        save_button = ttk.Button(self.inner_frame, text="Save", command=lambda: self.save_item(category, item))
        save_button.pack(pady=10)

    def add_new_item(self, category):
        # Clear previous details
        for widget in self.inner_frame.winfo_children():
            widget.pack_forget()

        # Create empty details for new item
        self.labels = {}
        self.entries = {}

        row = 0
        fields = {
            "movies": ["Title", "Studio", "Director", "Year", "Main Characters", "Genre", "Resolution"],
            "games": ["Title", "Company", "Genre", "Platform", "Release Date"],
            "books": ["Title", "Author", "Published Date", "Genre", "Edition", "Language", "Publisher"]
        }

        for field in fields[category]:
            label = ttk.Label(self.inner_frame, text=f"{field}:")
            label.pack(padx=5, pady=5, anchor="w")
            self.labels[field] = label

            entry = ttk.Entry(self.inner_frame)
            entry.pack(fill=tk.X, padx=5, pady=5)
            self.entries[field] = entry

            row += 1

        # Save button at the bottom
        save_button = ttk.Button(self.inner_frame, text="Save", command=lambda: self.save_new_item(category))
        save_button.pack(pady=10)

    def save_new_item(self, category):
        new_item = {key: entry.get() for key, entry in self.entries.items()}
        self.manager.add_item(category, new_item)
        messagebox.showinfo("Success", f"New {category.capitalize()} added successfully.")
        self.update_items_listbox(category)

    def save_item(self, category, item):
        updated_item = {key: entry.get() for key, entry in self.entries.items()}
        index = self.manager.get_items(category).index(item)
        self.manager.update_item(category, index, updated_item)
        messagebox.showinfo("Success", f"{category.capitalize()} updated successfully.")
        self.update_items_listbox(category)

    def delete_item(self, category):
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            item = self.manager.get_items(category)[index]
            confirmed = messagebox.askyesno("Delete Confirmation", f"Are you sure you want to delete {item.get('title', item.get('Title', item.get('name', '')))}?")
            if confirmed:
                self.manager.delete_item(category, index)
                messagebox.showinfo("Success", f"{category.capitalize()} deleted successfully.")
                self.update_items_listbox(category)
        else:
            messagebox.showwarning("Warning", "Select an item to delete.")

    def search_items(self, category):
        query = self.search_var.get().strip().lower()  # Get the search query from the Entry widget
        if query:
            results = self.manager.search_items(category, query)
        else:
            results = self.manager.get_items(category)

        # Clear current items in the listbox
        self.items_listbox.delete(0, tk.END)

        # Insert the filtered results into the listbox
        for item in results:
            if category == "movies":
                self.items_listbox.insert(tk.END, item.get('Title', "Unknown"))
            elif category == "games":
                self.items_listbox.insert(tk.END, item.get('Title', "Unknown"))  # Use 'Title' for games
            elif category == "books":
                self.items_listbox.insert(tk.END, item.get('Title', "Unknown"))  # Use 'title' for books
            else:
                self.items_listbox.insert(tk.END, "Unknown")

if __name__ == "__main__":
    manager = CollectionManager("collections.json")
    root = tk.Tk()
    app = CollectionApp(root, manager)
    root.mainloop()
