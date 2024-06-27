import tkinter as tk
from tkinter import messagebox, simpledialog
from business_layer import CollectionService
from data_layer import CollectionManager  # Import CollectionManager from data_layer

class CollectionApp:
    def __init__(self, root, service):
        self.root = root
        self.service = service

        self.root.title("Collection Manager")

        self.category_var = tk.StringVar(value="movies")
        self.search_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        # Category selection
        categories = ["movies", "games", "books"]
        tk.Label(self.root, text="Category:").grid(row=0, column=0)
        self.category_menu = tk.OptionMenu(self.root, self.category_var, *categories)
        self.category_menu.grid(row=0, column=1)

        # Search
        tk.Label(self.root, text="Search:").grid(row=1, column=0)
        self.search_entry = tk.Entry(self.root, textvariable=self.search_var)
        self.search_entry.grid(row=1, column=1)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_items)
        self.search_button.grid(row=1, column=2)

        # Items list with scrollbar
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.grid(row=2, column=3, sticky='ns')
        self.items_listbox = tk.Listbox(self.root, width=100, yscrollcommand=self.scrollbar.set)
        self.items_listbox.grid(row=2, column=0, columnspan=3)
        self.scrollbar.config(command=self.items_listbox.yview)
        self.update_items_listbox()

        # Buttons for CRUD operations
        self.add_button = tk.Button(self.root, text="Add", command=self.add_item)
        self.add_button.grid(row=3, column=0)
        self.update_button = tk.Button(self.root, text="Update", command=self.update_item)
        self.update_button.grid(row=3, column=1)
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_item)
        self.delete_button.grid(row=3, column=2)

    def update_items_listbox(self):
        self.items_listbox.delete(0, tk.END)
        category = self.category_var.get()
        items = self.service.get_items(category)
        for item in items:
            display_text = self.format_item_text(item)
            self.items_listbox.insert(tk.END, display_text)

    def format_item_text(self, item):
        if 'title' in item:
            return f"{item['title']} - {', '.join(f'{key}: {value}' for key, value in item.items() if key != 'title')}"
        else:
            return str(item)

    def add_item(self):
        category = self.category_var.get()
        item_info = self.prompt_for_item_info(category)
        if item_info:
            self.service.add_item(category, item_info)
            self.update_items_listbox()

    def update_item(self):
        category = self.category_var.get()
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            current_item = self.service.get_items(category)[index]
            self.prompt_for_item_info(category, current_item)  # Pass current_item to populate the entry fields
            self.update_items_listbox()
        else:
            messagebox.showwarning("Warning", "Select an item to update.")

    def delete_item(self):
        category = self.category_var.get()
        selected_index = self.items_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.service.delete_item(category, index)
            self.update_items_listbox()
        else:
            messagebox.showwarning("Warning", "Select an item to delete.")

    def search_items(self):
        category = self.category_var.get()
        query = self.search_var.get()
        results = self.service.search_items(category, query)
        self.items_listbox.delete(0, tk.END)
        for item in results:
            display_text = self.format_item_text(item)
            self.items_listbox.insert(tk.END, display_text)

    def prompt_for_item_info(self, category, current_item=None):
        fields = {
            "movies": ["Title", "Studio", "Director", "Year", "Main Characters", "Genre", "Resolution"],
            "games": ["Title", "Company", "Genre", "Platform", "Release Date"],
            "books": ["Title", "Author", "Published Date", "Genre", "Edition", "Language", "Publisher"]
        }
        popup = tk.Toplevel(self.root)
        popup.title(f"Enter {category[:-1].capitalize()} Information")

        item_info = {}
        entries = {}

        for field in fields[category]:
            field_key = field.lower().replace(" ", "_")
            current_value = current_item.get(field_key, "")
            tk.Label(popup, text=f"{field}:").pack()
            entry = tk.Entry(popup)
            entry.pack()
            entry.insert(0, current_value)
            entries[field_key] = entry

        save_button = tk.Button(popup, text="Save", command=lambda: self.save_item_info(category, current_item, entries))
        save_button.pack()

    def save_item_info(self, category, current_item, entries):
        new_item_info = {key: entry.get() for key, entry in entries.items()}
        if current_item:
            index = self.service.get_items(category).index(current_item)
            self.service.update_item(category, index, new_item_info)
        else:
            self.service.add_item(category, new_item_info)

        self.update_items_listbox()

if __name__ == "__main__":
    manager = CollectionManager("collections.json")
    service = CollectionService(manager)
    root = tk.Tk()
    app = CollectionApp(root, service)
    root.mainloop()
