import tkinter as tk
from pathlib import Path
from tkinter import filedialog

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_collection = None
        self.current_item = None

    def search(self):
        if not self.current_collection:
            self.view.show_error("Please select a collection first.")
            return
        query = self.view.search_entry.get()
        results = self.model.search_items(query, self.current_collection)
        self.update_item_list(results)

    def select_collection(self, collection_name):
        self.current_collection = collection_name
        items = self.model.get_items(collection_name)
        self.update_item_list(items)
        self.view.show_right_side()
        self.view.clear_info_fields()
        self.view.disable_edit_genres_button()
        self.current_item = None

    def update_item_list(self, items):
        self.view.item_listbox.delete(0, 'end')
        for index, item in enumerate(items, start=1):
            self.view.item_listbox.insert('end', f"{index}. {item.title}")

    def on_item_select(self, event):
        selection = self.view.item_listbox.curselection()
        if selection:
            index = int(selection[0])
            selected_title = self.view.item_listbox.get(index)
            selected_title = selected_title.split(". ", 1)[1]  # Remove the index number
            self.current_item = next((item for item in self.model.get_items(self.current_collection) if item.title == selected_title), None)
            if self.current_item:
                self.display_item_info()
                self.view.enable_edit_genres_button()

    def display_item_info(self):
        if self.current_item:
            info = {k: v for k, v in vars(self.current_item).items() if not k.startswith('_')}
            self.view.create_info_fields(info)
            self.view.update_image(self.current_item.image_path)
            self.view.description_text.delete("1.0", tk.END)
            self.view.description_text.insert(tk.END, self.current_item.description)
            self.view.save_button.config(state="disabled")

    def create_new_item(self):
        if self.current_collection:
            new_item = self.model.create_new_item(self.current_collection)
            self.current_item = new_item
            self.display_item_info()
            self.update_item_list(self.model.get_items(self.current_collection))

    def delete_item(self):
        if self.current_item:
            if self.view.ask_yes_no(f"Are you sure you want to delete {self.current_item.title}?"):
                self.model.remove_item(self.current_collection, self.current_item)
                self.current_item = None
                self.update_item_list(self.model.get_items(self.current_collection))
                self.view.create_info_fields({})

    def select_image(self):
        if self.current_item:
            initial_dir = Path(__file__).parent  # Start in the directory of the Python file
            file_path = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
            if file_path:
                self.current_item.image_path = file_path
                self.view.update_image(file_path)
                self.view.save_button.config(state="normal")

    def on_field_edit(self, event):
        self.view.save_button.config(state="normal")

    def save_item(self):
        if self.current_item:
            for key, entry in self.view.info_fields.items():
                if key != "Genres":
                    setattr(self.current_item, key, entry.get())
            self.current_item.description = self.view.description_text.get("1.0", tk.END).strip()
            self.model.save_data()
            self.view.show_info("Item saved successfully")
            self.view.save_button.config(state="disabled")
            self.update_item_list(self.model.get_items(self.current_collection))
            
    def open_genre_selection(self):
        if self.current_item and self.current_collection:
            genres = self.model.get_genres(self.current_collection)
            selected_genres = getattr(self.current_item, "Genres", [])
            self.view.show_genres_popup(genres, selected_genres)
            
    def update_genres(self, genre_vars, popup):
        selected_genres = [genre for genre, var in genre_vars.items() if var.get()]
        self.current_item.Genres = selected_genres
        self.view.update_genre_label(selected_genres)
        self.view.save_button.config(state="normal")
        popup.destroy()

    def save_genres(self, genre_vars, popup):
        selected_genres = [genre for genre, var in genre_vars.items() if var.get()]
        self.current_item.Genres = selected_genres
        self.view.info_fields["Genres"].config(text=f"Genres ({len(selected_genres)})")
        self.view.save_button.config(state="normal")
        popup.destroy()
